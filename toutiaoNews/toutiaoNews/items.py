# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ToutiaonewsItem(scrapy.Item):
    title = scrapy.Field()  # 新闻标题
    abstract = scrapy.Field()   # 摘要
    tag = scrapy.Field()    # 中文标签
    source_url = scrapy.Field() # 详情页url
    _id = scrapy.Field()
