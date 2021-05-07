from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from db_settings import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER


engine = create_engine(f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8')
Base = declarative_base()


class YHAnimeTB(Base):
    __tablename__ = 'YHAnime'

    name = Column('name', String(100), default='为空', comment='动漫名')
    anime_url = Column('anime_url', String(100), primary_key=True, comment='动漫详情页面url')
    score = Column('score', String(10), default='0.0分', comment='评分')
    publish_date = Column('publish_date', String(20), comment='上映日期')
    location = Column('location', String(20), default='暂缺', comment='地区')
    type_of_anime = Column('type_of_anime', String(100), default='暂缺', comment='动漫分类，可能有多个类别')
    tags = Column('tags', String(100), comment='标签，感觉和分类会有重叠，个人不是动漫迷，不懂行')
    desc = Column('desc', Text, default='暂缺', comment='简介')
    source_urls = Column('source_urls', Text, default='暂缺', comment='动漫播放页的链接')
    crawl_time = Column('crawl_time', DateTime, comment='爬取时间')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)