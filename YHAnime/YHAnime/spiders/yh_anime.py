import re
from datetime import datetime
from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from items import YhanimeItem


class YhAnimeSpider(CrawlSpider):
    name = 'yh_anime'
    allowed_domains = ['yhdm.so']
    start_urls = ['http://www.yhdm.so/']

    rules = (
        Rule(LinkExtractor(allow=r'/show/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        name = response.xpath('//h1/text()').extract_first()
        score = response.xpath('//div[@class="score"]//em//text()').extract_first()
        anime_info = response.xpath('//div[@class="sinfo"]//text()').extract()
        REGEX_INFO = re.compile(r'上映:(.*?)地区:(.*?)类型:(.*?)索引:.*?标签:(.*?)评论:')
        anime_info = REGEX_INFO.findall(' '.join(''.join(anime_info).split()))
        publish_date, location, type_of_anime, tags = anime_info[0]
        desc = response.xpath('//div[@class="info"]//text()').extract_first()
        movurls = response.xpath('//div[@class="tabs"]//div[@class="movurl"]//a/@href').extract()
        crawl_time = datetime.now()
        movurls = [urljoin(response.url, movurl) for movurl in movurls]
        item = YhanimeItem(
            name=name,
            score=score,
            publish_date=publish_date,
            localtion=location,
            type_of_anime=type_of_anime,
            tags=tags,
            desc=desc,
            source_urls=movurls,
            crawl_time=crawl_time
            )
        yield item
        