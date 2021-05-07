import scrapy


class YhanimeItem(scrapy.Item):
    """樱花动漫
    Args:
        name(str): 动漫的名称
        anime_url(str): 动漫详情页面url
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
    anime_url = scrapy.Field()
    score = scrapy.Field()
    publish_date = scrapy.Field()
    location = scrapy.Field()
    type_of_anime = scrapy.Field()
    tags = scrapy.Field()
    desc = scrapy.Field()
    source_urls = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO YHAnime(`name`, `anime_url`, `score`, `publish_date`, `location`,
            `type_of_anime`, `tags`, `desc`, `source_urls`, `crawl_time`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            `source_urls`=VALUES (`source_urls`)
        """
        params = (
            self['name'],
            self['anime_url'],
            self['score'],
            self['publish_date'],
            self['location'],
            self['type_of_anime'],
            self['tags'],
            self['desc'],
            self['source_urls'],
            self['crawl_time']
        )
        return insert_sql, params