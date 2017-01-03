import scrapy
from scrapy.crawler import CrawlerProcess
import logging

class TheaterM_gallery_Crawler(scrapy.Spider):
    name = 'DC Inside Theater Musical gallery recommend'
    # 크롤러의 이름
    start_urls = ['http://gall.dcinside.com/board/lists/?id=theaterM&page=1&exception_mode=recommend']
    # 크롤링 하려는 URL
    base_urls = 'http://gall.dcinside.com'
    #출력형식의 URL 앞부분!
    logging.getLogger('scrapy').propagate = False
    #위 줄이 있으면 Scrapy에서의 log를 제외한 크롤링 결과만 출력됩니다.
    
    def parse(self, response):
        title = '.list_thead > tr > td:nth-child(2) > a::text'
        #제목입니다.
        number = '.list_thead > tr > td:nth-child(1)::text'
        #고유번호입니다. 고유번호는 계속 증가해야 해요
        href = '.list_thead > tr > td:nth-child(2) > a:nth-child(1)::attr(href)'
        #글 링크
        numbers = [int(text) for text in response.css(number).extract() if text.isdigit()]
        titles = response.css(title).extract()[4:]
        refs = (response.css(href).extract())[6:]
        results = zip(numbers, titles, refs)
        
        for number, title, ref in results:
            print(str(number) + "&^%987&^%" + title + "&^%987&^%" + self.base_urls + ref)
        #출력할 때는 고유번호 seperator 제목 seperator 글 링크 형식에 맞춰야 해요 

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TheaterM_gallery_Crawler)
process.start()
