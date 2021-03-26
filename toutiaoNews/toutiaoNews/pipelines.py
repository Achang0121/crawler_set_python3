import pymongo
from itemadapter import ItemAdapter


class ToutiaonewsPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline:

    def __init__(self, mongo_uri, mongo_db, mongo_col):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_col = mongo_col

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI', 'mongodb://127.0.0.1:27017/'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_col=crawler.settings.get('MONGODB_COL')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.mongodb = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.mongodb[self.mongo_col].insert(dict(item))
        return item
