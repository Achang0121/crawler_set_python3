# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from JavBus.settings import MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER

engine = create_engine(f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8")

Base = declarative_base()


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
