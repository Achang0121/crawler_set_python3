import datetime

import scrapy
from scrapy.loader.processors import MapCompose


def date_format_convert(value):
    try:
        update_time = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except Exception as e:
        print(e)
        update_time = datetime.datetime.now()
    return update_time


class JavBusItem(scrapy.Item):
    name = scrapy.Field()  # 片名
    url = scrapy.Field()  # 详情页url
    cover_image = scrapy.Field()  # 封面图链接
    serial_number = scrapy.Field()  # 番号
    is_censored = scrapy.Field()  # 骑兵还是步兵
    duration = scrapy.Field()  # 时长
    actors = scrapy.Field()  # 参演者
    manufacturer = scrapy.Field()  # 制作商
    series = scrapy.Field()  # 系列
    category = scrapy.Field()  # 类别
    magnetic_connection = scrapy.Field()  # 磁力链接
    crawl_time = scrapy.Field()  # 爬取时间
    update_time = scrapy.Field(
        input_porcessor=MapCompose(date_format_convert)
    )  # 更新时间
    
    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO jav_bus(name, url, cover_image, serial_number, crawl_time, update_time, is_censored,
            actors, series, category, magnetic_connection, manufacturer, duration)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            name =VALUES (name), url=VALUES (url), cover_image=VALUES (cover_image),
            serial_number=VALUES (serial_number), actors=VALUES (actors), series=VALUES (series),
            category=VALUES (category), magnetic_connection=VALUES (magnetic_connection),
            manufacturer=VALUES (manufacturer), duration=VALUES (duration)
        """
        params = (
            self['name'],
            self['url'],
            self['cover_image'],
            self['serial_number'],
            self['crawl_time'],
            self['update_time'],
            self['is_censored'],
            self['actors'],
            self['series'],
            self['category'],
            self['magnetic_connection'],
            self['manufacturer'],
            self['duration']
        )
        return insert_sql, params
