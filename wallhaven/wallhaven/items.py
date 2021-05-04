import scrapy


class WallhavenItem(scrapy.Item):
    collection = "wallhaven_images"
    source_url = scrapy.Field() # 完整图片源地址
    tags = scrapy.Field()   # 图片的标签
    thumbnail = scrapy.Field()  # 网站为图片生成的唯一代码

