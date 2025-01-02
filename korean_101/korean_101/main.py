from spiders.login import LoginSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


process = CrawlerProcess(get_project_settings())

# Gọi các spider
process.crawl(LoginSpider)
process.start()  # Chạy spider đăng nhập
