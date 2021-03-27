import re

import scrapy

from wallhaven.items import WallhavenItem


class WallHavenSpider(scrapy.Spider):
    name = 'wall_haven'
    allowed_domains = ['www.wallhaven.cc']
    start_urls = ['https://wallhaven.cc/latest?page=1']

    # def start_requests(self):
    #     for page in range(1, self.settings.get("MAX_PAGE")+1):
    #         url = f'https://wallhaven.cc/latest?page={page}'
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        current_page = re.search(r'.*?page=(\d+)$', response.url).group(1)
        elements = response.xpath('//a[@class="preview"]/@href').extract()
        for element in elements:
            yield scrapy.Request(url=element, callback=self.parse_detail, dont_filter=True)

        if int(current_page) < self.settings.get("MAX_PAGE"):
            next_url = f'https://wallhaven.cc/latest?page={int(current_page)+1}'
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):
        tags = '; '.join(response.xpath('//ul[@id="tags"]/li/a/text()').extract())
        source_url = response.xpath('//img[@id="wallpaper"]/@src').extract_first()
        thumbnail = response.url.split('/')[-1]

        item = WallhavenItem(source_url=source_url, tags=tags, thumbnail=thumbnail)
        yield item
