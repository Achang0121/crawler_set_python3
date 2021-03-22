from datetime import datetime
import re
from urllib.parse import urljoin

import scrapy
from JavBus.items import JavBusItem


class JavBusSpider(scrapy.Spider):
    name = 'javBus'
    allowed_domains = ['javbus.com', 'javbus.one']
    start_urls = ['https://www.javbus.com/', 'https://www.javbus.com/uncensored', 'https://www.javbus.one/']
    
    def parse(self, response, **kwargs):
        movies = response.xpath('//a[@class="movie-box"]')
        next_page_url = urljoin(response.url, response.xpath('//a[@id="next"]/@href').extract_first())
        is_consored_flag = response.xpath('//ul[contains(@class, "nav")]//li[@class="active"]/a/text()').extract_first()
        for movie in movies:
            item = JavBusItem()
            item['name'] = movie.xpath('.//img/@title').extract_first()
            item['url'] = movie.xpath('./@href').extract_first()
            item['cover_image'] = movie.xpath('.//img/@src').extract_first()
            item['serial_number'] = item['url'].split("/")[-1]
            item['is_censored'] = 1 if is_consored_flag == "有碼" else 0
            item['crawl_time'] = datetime.now()
            item['update_time'] = movie.xpath('.//date[2]/text()').extract_first()
            yield scrapy.Request(url=item['url'], meta={"item": item}, callback=self.parse_detail)
        yield scrapy.Request(url=next_page_url)
    
    def parse_detail(self, response):
        item = response.meta.get("item")
        movie_info = response.xpath('//div[contains(@class, "movie")][1]//text()').extract()
        movie_info_string = " ".join(" ".join(movie_info).strip().split())
        duration = re.match(r".*?長度:(.*?)分鐘.*?", movie_info_string)
        item['duration'] = duration.groups()[0] if duration else " "
        manufacturer = re.match(".*?製作商:(.*?)發行商.*?", movie_info_string)
        item['manufacturer'] = manufacturer.groups()[0] if manufacturer else " "
        series = re.match(".*?系列:(.*?)類別:.*?", movie_info_string)
        item['series'] = series.groups()[0] if series else " "
        category = re.match(".*?類別:(.*?)演員.*?", movie_info_string)
        item['category'] = category.groups()[0] if category else " "
        # 下面两个是ajax请求的
        # item['actors'] = re.match(r".*?演員 :(.*?)", movie_info_string).groups()[0]
        # item['magnetic_connection'] = response.xpath('//table[@id="magnet-table"]//a/@href').extract()
        item['actors'] = " "
        item['magnetic_connection'] = " "
        
        return item
