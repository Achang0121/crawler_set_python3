import requests
# from lxml import etree
import re
from urllib.parse import urljoin


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}


class SeHuaTangBook:

    def __init__(self, target_url: str):
        self.session = requests.session()
        self.target_url = target_url
        self.session.headers = HEADERS
        self.session.verify = False


    def run(self):
        response = self.session.get(self.target_url)
        title = self.fetch_title(response)
        self.title = title
        chapter_urls = self.fetch_capter_url(response)
        for chapter_url in chapter_urls:
            chapter_response = self.session.get(chapter_url)
            data = self.fetch_chapter_content(chapter_response)
            self.download_text(data, title)

    def get_title(self):
        return self.title
            
    def fetch_chapter_content(self, response):
        """解析小说内容"""    
        REGEX_CHAPTER = re.compile(r'<p>(.*?)</p>')
        data = REGEX_CHAPTER.findall(response.text)
        return data

    def fetch_capter_url(self, response):
        """获取章节的链接并返回完整的链接列表"""
        REGEX_CHAPTER_URL = re.compile(r'<a href="(.*?)" target="_blank">\d+</a>')
        urls = REGEX_CHAPTER_URL.findall(response.text)
        return [urljoin(response.url, url) for url in urls][1:]

    def fetch_title(self, response):
        REGEX_TITLE = re.compile(r'<h1>(.*?)</h1>')
        title = REGEX_TITLE.findall(response.text)[0]
        return title

    def download_text(self, content, file_name):
        with open(f'./novels/{file_name}.txt', 'a', encoding='utf-8') as f:
            for line in content:
                f.write(line.strip().replace('\u3000', '').replace('\xa0', '').replace('<br>', '\n').replace('&nbsp;', ''))
            f.write('\n')




if __name__ == '__main__':
    stb1 = SeHuaTangBook('https://www.sehuatang.org/book-1446.html')
    stb1.run()