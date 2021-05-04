# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from db_settings import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER

engine = create_engine(f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8")

Base = declarative_base()


class JavBus(Base):
    __tablename__ = 'jav_bus'

    name = Column('name', String(500), comment="影片标题")
    url = Column('url', String(200), comment="详情页链接")
    cover_image = Column('cover_image', String(100), comment="封面图链接")
    serial_number = Column('serial_number', String(50), primary_key=True, comment="影片番号")
    is_censored = Column('is_censored', Integer, default=1, comment="骑兵or步兵")
    duration = Column('duration', String(20), comment="影片时长")
    actors = Column('actors', String(1000), default=' ', comment="演员表")
    manufacturer = Column('manufacturer', String(50), default=' ', comment="制作商")
    series = Column('series', String(1000), default=' ', comment="影片系列")
    category = Column('category', String(1000), default=' ', comment="影片类别")
    magnetic_connection = Column('magnetic_connection', String(2000), default=' ', comment="资源磁力链接")
    crawl_time = Column('crawl_time', String(50), comment="爬取时间")
    update_time = Column('update_time', DateTime(), comment="更新时间")


class JavBusActress(Base):
    __tablename__ = "jav_bus_actress"
    
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    actress_photo = Column("actress_photo", String(100), nullable=True, default=" ")  # 演员头像
    actress_personal_url = Column("actress_personal_url", String(100), nullable=True, default=" ")  # 演员参演作品集合页面链接
    actress_name = Column("actress_name", String(50), nullable=False, unique=True)
    actress_birthday = Column("actress_birthday", String(10), nullable=True, default=" ")
    actress_age = Column("actress_age", String(10), nullable=True, default="18")
    actress_height = Column("actress_height", String(10), nullable=True, default="168")
    actress_cup = Column("actress_cup", String(10), nullable=True, default="B")
    actress_bust = Column("actress_bust", String(10), nullable=True, default="80")
    actress_waist = Column("actress_waist", String(10), nullable=True, default="60")
    actress_hip = Column("actress_hip", String(10), nullable=True, default="80")
    actress_hobbies = Column("actress_hobbies", String(50), nullable=True, default=" ")
    actress_native = Column("actress_native", String(20), nullable=True, default=" ")
    crawl_time = Column("crawl_time", String(50))
    
    def __repr__(self):
        return f"Name: {self.actress_name}"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
