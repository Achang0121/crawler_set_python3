BOT_NAME = 'wallhaven'

SPIDER_MODULES = ['wallhaven.spiders']
NEWSPIDER_MODULE = 'wallhaven.spiders'

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

ITEM_PIPELINES = {
   'wallhaven.pipelines.MongoDBPipeline': 300,
   'wallhaven.pipelines.DownloadImagePipeline': 100,
}

IMAGES_STORE = './images'

MAX_PAGE = 1   # ajax请求的唯一参数，这老外的网站反爬真没啥，全靠自觉，速度太快会出问题，尽量友好点

CONCURRENT_REQUESTS = 4
RANDOMSIZE_DOWNLOAD_DEALY = True
DOWNLOAD_TIMEOUT = 100
COOKIES_ENABLED = False


MOMGO_URI = "mongodb://127.0.0.1:27017"
MONGO_DB = "wallheaven"

import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'wallhaven'))