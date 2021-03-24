import sys
import os

BOT_NAME = 'JavBus'

SPIDER_MODULES = ['JavBus.spiders']
NEWSPIDER_MODULE = 'JavBus.spiders'

# 频率设置
CONCURRENT_REQUESTS = 32
CONCURRENT_ITEMS = 16
DOWNLOAD_TIMEOUT = 10

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = False

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'JavBus.middlewares.JavbusSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'JavBus.middlewares.JavbusDownloaderMiddleware': 100,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'JavBus.pipelines.MySQLTwistedPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 301
}

# mysql 的一些配置
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'jav_bus'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'

SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SQL_DATE_FORMAT = "%Y-%m-%d"

TELNETCONSOLE_USERNAME = "cjm"
TELNETCONSOLE_PASSWORD = "123456"

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "JavBus"))

# scrapy-redis 的配置
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
REDIS_URL = 'redis://localhost:6379'
