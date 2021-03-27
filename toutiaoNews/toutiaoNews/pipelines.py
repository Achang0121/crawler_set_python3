import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
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
        self.connection = AsyncIOMotorClient(self.mongo_uri)
        self.mongodb = self.connection[self.mongo_db]

    def process_item(self, item, spider):
        asyncio.get_event_loop().run_until_complete(self._insert(item))
        return item

    async def _insert(self, item):
        await self.mongodb[self.mongo_col].insert_one(item)
