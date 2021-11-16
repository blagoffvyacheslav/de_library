from scrapy.crawler import CrawlerProcess # maim process
from scrapy.settings import Settings # main settings

from diploma import settings # project settings
from diploma.spiders.dnb import DnbSpider # spider

if __name__ == '__main__':
    crawler_settings = Settings() # global settings
    crawler_settings.setmodule(settings) # local settings

    process = CrawlerProcess(settings = crawler_settings) # settings for spider for accepting
    process.crawl(DnbSpider) # links process and spider

    process.start()

