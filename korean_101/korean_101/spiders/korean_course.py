import scrapy
from selenium.webdriver.common.by import By
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
import time
 
class KoreanSpider(scrapy.Spider):
    name = 'korean_course'
    allowed_domains = ["koreanclass101.com"]
    # start_urls = ["https://www.koreanclass101.com/lesson-library/absolute-beginner"] # Replace with your target URL
 
    # def parse(self, response):
    #     courses = response.xpath('//div[@class="list"]/a[contains(@class, "ll-collection-all")]/div/div[@class="ll-collection-all__table"]')
       
    #     for course in courses:
    #         media_type = ''
    #         if course.xpath('.//span[contains(@class, "ll-collection-all__type--Audio")]'):
    #             media_type = "Audio"
    #         elif course.xpath('.//span[contains(@class, "ll-collection-all__type--Mixed")]'):
    #             media_type = "Mixed"
    #         else:
    #              media_type = "Video"
               
    #         yield {
    #             'title': course.xpath('.//div[contains(@class, "ll-collection-all__title")]/text()').get(),
    #             'description': course.xpath('.//div[contains(@class, "ll-collection-all__description")]/span/text()').get(),
    #             'lessons': course.xpath('.//span[contains(@class, "ll-collection-all__lessons")]/text()').get(),
    #             'media_type': media_type,
    #         }
 
    start_urls = ["https://www.koreanclass101.com/lesson-library/3-minute-korean-greetings-and-useful-phrases"]
    def parse(self, response):
        lessons = response.xpath('//div[@class="_row_181ys_207"]')
        driver = webdriver.Chrome()
        # driver = response.request.meta['driver']
 
 
       
        for lesson in lessons:
            title = lesson.xpath('.//a[@class="_lesson__link_1h6vq_27"]/div[@class="_lesson__middle_1h6vq_119"]/h2[@class="_lesson__title_1h6vq_14"]/text()').get()
            href = response.urljoin(lesson.xpath('.//a[@class="_lesson__link_1h6vq_27"]/@href').get())
            driver.get(href)
            time.sleep(10)
            yield {
                'title': title,
                'link': href
            }
            