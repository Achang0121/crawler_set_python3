import pymongo
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MongoDBPipeline:
    """存入mongodb"""

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MOMGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item


class DownloadImagePipeline(ImagesPipeline):
    """图片下载"""
    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_pathes = [x['path'] for ok, x in results if ok]
        if not image_pathes:
            raise DropItem("图片下载失败")
        return item

    def get_media_requests(self, item, info):
        yield Request(item['source_url'])
