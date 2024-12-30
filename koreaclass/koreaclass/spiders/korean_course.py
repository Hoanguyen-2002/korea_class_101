import scrapy

class KoreanSpider(scrapy.Spider):
    name = 'korean_course'
    allowed_domains = ["koreanclass101.com"]
    start_urls = ["https://www.koreanclass101.com/lesson-library/absolute-beginner"] # Replace with your target URL

    def parse(self, response):
        courses = response.xpath('//div[@class="list"]/a[contains(@class, "ll-collection-all")]/div/div[@class="ll-collection-all__table"]')
        
        for course in courses:
            media_type = ''
            if course.xpath('.//span[contains(@class, "ll-collection-all__type--Audio")]'):
                media_type = "Audio"
            elif course.xpath('.//span[contains(@class, "ll-collection-all__type--Mixed")]'):
                media_type = "Mixed"
            else:
                 media_type = "Video"
                
            yield {
                'title': course.xpath('.//div[contains(@class, "ll-collection-all__title")]/text()').get(),
                'description': course.xpath('.//div[contains(@class, "ll-collection-all__description")]/span/text()').get(),
                'lessons': course.xpath('.//span[contains(@class, "ll-collection-all__lessons")]/text()').get(),
                'media_type': media_type, 
            }