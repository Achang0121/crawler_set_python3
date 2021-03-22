from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

crawler = CrawlerProcess(settings)

crawler.crawl('javBus')
# crawler.crawl('javBus_uncensored')

crawler.start()
# crawler.start()