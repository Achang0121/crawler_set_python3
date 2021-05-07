from pymysql.cursors import DictCursor
from twisted.enterprise import adbapi
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class YhanimeMySQLTwistedPipeline:
    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_crawler(cls, crawler):
        db_params = dict(
            host=crawler.settings.get("MYSQL_HOST"),
            database=crawler.settings.get("MYSQL_DATABASE"),
            user=crawler.settings.get("MYSQL_USER"),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
            charset='utf8',
            cursorclass=DictCursor,
            cp_min=32,
            cp_max=64,
            use_unicode=True
        )
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        return cls(db_pool=db_pool)

    def filter_item(self, result, item, spider):
        # 过滤item，数据库中存在的则直接返回，否则进行插入操作
        if result:
            raise DropItem(f"Duplicate item found")
        query = self.db_pool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def process_item(self, item, spider):
        query = self.db_pool.runQuery(
            "SELECT anime_url FROM YHAnime WHERE anime_url=%s",
            item['anime_url']
        )
        query.addCallback(self.filter_item, item, spider)
        query.addErrback(self.handle_error, item, spider)
        return item

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
