import json
from urllib.parse import urljoin

import scrapy
from toutiaoNews.items import ToutiaonewsItem

class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['toutiao.com']
    start_urls = ['https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=news_hot&utm_source=toutiao&widen=1&tadrequire=true']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Host': 'www.toutiao.com'
        }
    }
    
    def parse(self, response):
        results = json.loads(response.text)
        next_max_behot_time = results['next']['max_behot_time']
        for element in results['data']:
            item = ToutiaonewsItem()
            item['title'] = element.get('title')
            item['abstract'] = element.get('abstract')
            item['tag'] = element.get('chinese_tag')
            item['source_url'] = urljoin('https://www.toutiao.com', element.get('source_url'))
            yield item

        next_url = f'https://www.toutiao.com/api/pc/feed/?max_behot_time={next_max_behot_time}&category=news_hot&utm_source=toutiao&widen=1&tadrequire=true'
        yield scrapy.Request(url=next_url)