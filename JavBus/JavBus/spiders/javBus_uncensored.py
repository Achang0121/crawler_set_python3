from datetime import datetime
from urllib.parse import urljoin

import scrapy
from ..items import JavBusItem


class JavBusSpider(scrapy.Spider):
    name = 'javBus_uncensored'
    allowed_domains = ['javbus.com']
    start_urls = ['http://www.javbus.com/uncensored', ]
    
    def parse(self, response, **kwargs):
        movies = response.xpath('//a[@class="movie-box"]')
        next_page_url = urljoin(response.url, response.xpath('//a[@id="next"]/@href').extract_first())
        for movie in movies:
            item = JavBusItem()
            item['name'] = movie.xpath('.//img/@title').extract_first()
            item['url'] = movie.xpath('./@href').extract_first()
            item['cover_image'] = movie.xpath('.//img/@src').extract_first()
            item['serial_number'] = item['url'].split("/")[-1]
            item['is_censored'] = 1
            item['crawl_time'] = datetime.now()
            item['update_time'] = movie.xpath('.//date[2]/text()').extract_first()
            yield item
        yield scrapy.Request(url=next_page_url)
