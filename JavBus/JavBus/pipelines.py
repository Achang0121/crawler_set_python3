# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymysql.cursors import DictCursor
from twisted.enterprise import adbapi
from itemadapter import ItemAdapter


class JavBusPipeline:
    def process_item(self, item, spider):
        return item


class MySQLTwistedPipeline:
    
    def __init__(self, db_pool):
        self.db_pool = db_pool
    
    @classmethod
    def from_crawler(cls, crawler):
        db_params = dict(
            host=crawler.settings.get("MYSQL_HOST"),
            database=crawler.settings.get("MYSQL_DATABASE"),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
            charset='utf8',
            cursorclass=DictCursor,
            cp_min=32,
            cp_max=64,
            use_unicode=True
        )
        dp_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool=dp_pool)
    
    def filter_item(self, result, item, spider):
        # 过滤item，数据库中存在的则直接返回，否则进行插入操作
        if result:
            return item
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)
    
    def process_item(self, item, spider):
        query = None
        if spider.name == "javBus":
            query = self.db_pool.runQuery(
                "SELECT serial_number FROM jav_bus WHERE serial_number=%s",
                item['serial_number']
            )
        elif spider.name == "JavBusActress":
            query = self.db_pool.runQuery(
                "SELECT actress_name FROM jav_bus_actress where actress_name=%s",
                item['actress_name']
            )
        query.addCallback(self.filter_item, item, spider)
        query.addErrback(self.handle_error, item, spider)
        return item
    
    def handle_error(self, failure, item, spider):
        print(failure)
    
    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
