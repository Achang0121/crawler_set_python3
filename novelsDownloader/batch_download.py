import random
import time
import threading

import requests
import re
from lxml import etree
from urllib.parse import urljoin
import urllib3
from sht import SeHuaTangBook

urllib3.disable_warnings()


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}


class NovelCategory:
    def __init__(self, category_url):
        self.category_url = category_url
        self.session = requests.session()
        self.session.headers = HEADERS
        self.verify = False

    def run(self):
        response = self.session.get(self.category_url)
        novels = self.fetch_novel_detail_url(response)
        for novel in novels:
            shtb = SeHuaTangBook(novel)
            shtb.run()
            print(f'------《{shtb.get_title()}》 已下载完成 ------')

    def fetch_novel_detail_url(self, response):
        content = etree.HTML(response.text)
        novel_urls = content.xpath(
            '//div[@class="book_item"]//a[@class="title"]/@href')
        return [urljoin(response.url, novel_url) for novel_url in novel_urls]


def download_one_page(url):
    novel_category = NovelCategory(url)
    novel_category.run()


if __name__ == '__main__':
    # 这里我写死了，也可以发请求获取最大页面数字，差不太多吧
    urls = [f'https://www.sehuatang.org/book-category-2-{i}.html' for i in range(1, 56)]
    tasks = []
    for url in urls:
        task = threading.Thread(target=download_one_page, args=(url,))
        tasks.append(task)
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
