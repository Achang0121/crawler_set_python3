from datetime import datetime
import re
from urllib.parse import urljoin

import scrapy
from demo.items import JavBusItem


class JavBusSpider(scrapy.Spider):
    name = 'javBus'
    allowed_domains = ['javbus.com']
    start_urls = ['https://javbus.com/']
    
    def parse(self, response, **kwargs):
        movies = response.xpath('//a[@class="movie-box"]')
        next_page_url = urljoin(response.url, response.xpath('//a[@id="next"]/@href').extract_first())
        for movie in movies:
            item = JavBusItem()
            item['name'] = movie.xpath('.//img/@title').extract_first()
            item['url'] = movie.xpath('./@href').extract_first()
            item['cover_image'] = movie.xpath('.//img/@src').extract_first()
            item['serial_number'] = item['url'].split("/")[-1]
            item['is_censored'] = 0
            item['crawl_time'] = datetime.now()
            item['update_time'] = movie.xpath('.//date[2]/text()').extract_first()
            yield scrapy.Request(url=item['url'], meta={"item": item}, callback=self.parse_detail)
        # yield scrapy.Request(url=next_page_url)
    
    def parse_detail(self, response):
        item = response.meta.get("item")
        movie_info = response.xpath('//div[contains(@class, "movie")][1]//text()').extract()
        movie_info_string = " ".join(" ".join(movie_info).strip().split())
        item['duration'] = re.match(r".*?長度:(.*?)分鐘.*?", movie_info_string).groups()[0]
        item['manufacturer'] = re.match(".*?製作商:(.*?)發行商.*?", movie_info_string).groups()[0]
        item['series'] = re.match(".*?系列:(.*?)類別:.*?", movie_info_string).groups()[0]
        item['category'] = re.match(".*?類別:(.*?)演員.*?", movie_info_string).groups()[0]
        # 下面两个是ajax请求的
        item['actors'] = re.match(r".*?演員 :(.*?)", movie_info_string).groups()[0]
        # item['magnetic_connection'] = response.xpath('//table[@id="magnet-table"]//a/@href').extract()
    
        return item
