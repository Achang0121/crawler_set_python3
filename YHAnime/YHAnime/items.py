import scrapy


class YhanimeItem(scrapy.Item):
    """樱花动漫
    Args:
        name(str): 动漫的名称
        score(str): 该动漫的评分
        publish_date(date): 上映日期
        localtion(str): 地区
        type_of_anime(str): 动漫类型
        tags(str): 动漫标签 
        desc(str): 简介
        source_urls(list): 资源链接
        crawl_time(date): 抓取时间
    """
    name = scrapy.Field()
    score = scrapy.Field()
    publish_date = scrapy.Field()
    localtion = scrapy.Field()
    type_of_anime = scrapy.Field()
    tags = scrapy.Field()
    desc = scrapy.Field()
    source_urls = scrapy.Field()
    crawl_time = scrapy.Field()

