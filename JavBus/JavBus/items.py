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


class JavBusActressItem(scrapy.Item):
    # actress 基本信息
    actress_photo = scrapy.Field()  # 演员头像
    actress_personal_url = scrapy.Field()  # 演员参演作品集合页面链接
    actress_name = scrapy.Field()  # 演员名字
    actress_birthday = scrapy.Field()  # 生日
    actress_age = scrapy.Field()  # 年龄
    actress_height = scrapy.Field()  # 身高
    actress_cup = scrapy.Field()  # 欧派大小
    actress_bust = scrapy.Field()  # 胸围
    actress_waist = scrapy.Field()  # 腰围
    actress_hip = scrapy.Field()  # 臀围
    actress_hobbies = scrapy.Field()  # 兴趣
    actress_native = scrapy.Field()  # 出生地
    
    # 额外的参数
    crawl_time = scrapy.Field(
        input_porcessor=MapCompose(date_format_convert)
    )  # 爬取时间
    
    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO jav_bus_actress(actress_photo, actress_personal_url, actress_name, actress_birthday, actress_age,
            actress_height, actress_cup, actress_bust, actress_waist, actress_hip, actress_hobbies,
            actress_native, crawl_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            actress_personal_url=VALUES (actress_personal_url), actress_photo=VALUES (actress_photo),
            actress_hip=VALUES (actress_hip), actress_cup=VALUES (actress_cup), actress_bust=VALUES (actress_bust),
            actress_waist=VALUES (actress_waist)
        """
        params = (
            self['actress_photo'],
            self['actress_personal_url'],
            self['actress_name'],
            self['actress_birthday'],
            self['actress_age'],
            self['actress_height'],
            self['actress_cup'],
            self['actress_bust'],
            self['actress_waist'],
            self['actress_hip'],
            self['actress_hobbies'],
            self['actress_native'],
            self['crawl_time']
        )
        return insert_sql, params
