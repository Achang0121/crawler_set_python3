from datetime import datetime
import re
import random
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
        actors = response.xpath('//div[@class="star-name"]/a/@title').extract()
        item['actors'] = ' '.join(actors) if actors else ' '
        
        # 构造ajax请求，获取magnet
        headers = {
            'Host': 'www.javbus.com',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Refer': 'https://www.javbus.com/SSIS-013',
        }
        site_text = response.text
        lang = re.search(r'.*?var\slang\s=\s\'(.*?)\';.*?', site_text, re.M).groups()[0]
        gid = re.search(r'.*?var\sgid\s=\s(.*?);.*?', site_text, re.M).groups()[0]
        uc = re.search(r'.*?var\suc\s=\s(.*?);.*?', site_text, re.M).groups()[0]
        img = re.search(r'.*?var\simg\s=\s\'(.*?)\';.*?', site_text, re.M).groups()[0]
        magnet_url = f"https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid={gid}&lang={lang}&img={img}&uc={uc}&floor={int(random.random() * 1000) + 1}"
        yield scrapy.Request(url=magnet_url, meta={'item': item}, headers=headers, callback=self.get_magnet)
    
    def get_magnet(self, response):
        # 可能会有重复的magnet，用set去重
        magnets = set(response.xpath('//a/@href').extract())
        item = response.meta.get('item')
        item['magnetic_connection'] = ' '.join(magnets)
        return item
