import datetime
import re

import scrapy

from JavBus.items import JavBusActressItem


class JavbusactressSpider(scrapy.Spider):
    name = 'JavBusActress'
    allowed_domains = ['javbus.com']
    start_urls = ['https://www.javbus.com/actresses']

    def parse(self, response, **kwargs):
        actress_list = response.xpath('//div[contains(@class, "item")]')
        for actress in actress_list:
            item = JavBusActressItem()
            item['actress_photo'] = actress.xpath('.//div[@class="photo-frame"]/img/@src').extract_first()
            item['actress_name'] = actress.xpath('.//div[@class="photo-info"]/span/text()').extract_first()
            item['actress_personal_url'] = actress.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=item['actress_personal_url'], meta={'item': item}, callback=self.parse_personal_web)
            
    def parse_personal_web(self, response):
        item = response.meta.get("item")
        actress_info = '|'.join(response.xpath('//div[@class="photo-info"]//p/text()').extract())
        birthday = re.search(r'生日:(.*?)\|', actress_info)
        item['actress_birthday'] = birthday.groups()[0] if birthday else " "
        actress_age = re.search(r'年齡:(.*?)\|', actress_info)
        item['actress_age'] = actress_age.groups()[0] if actress_age else " "
        actress_height = re.search(r'身高:(.*?)cm\|', actress_info)
        item['actress_height'] = actress_height.groups()[0] if actress_height else " "
        actress_cup = re.search(r'罩杯:(.*?)\|', actress_info)
        item['actress_cup'] = actress_cup.groups()[0] if actress_cup else " "
        actress_bust = re.search(r'胸圍:(.*?)cm\|', actress_info)
        item['actress_bust'] = actress_bust.groups()[0] if actress_bust else " "
        actress_waist = re.search(r'腰圍:(.*?)cm\|', actress_info)
        item['actress_waist'] = actress_waist.groups()[0] if actress_waist else " "
        actress_hip = re.search(r'臀圍:(.*?)cm\|', actress_info)
        item['actress_hip'] = actress_hip.groups()[0] if actress_hip else " "
        actress_hobbies = re.search(r'愛好:(.*?)$', actress_info)
        item['actress_hobbies'] = actress_hobbies.groups()[0] if actress_hobbies else " "
        actress_native = re.search(r'出生地:(.*?)\|', actress_info)
        item['actress_native'] = actress_native.groups()[0] if actress_native else " "
        item['crawler_time'] = datetime.datetime.now()
        return item
