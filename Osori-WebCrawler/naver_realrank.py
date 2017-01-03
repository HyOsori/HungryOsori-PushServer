import scrapy
from scrapy.crawler import CrawlerProcess
import datetime
import logging

class NaverRealRankCrawler(scrapy.Spider):
    name = 'naver realrank'
    start_urls = ['http://www.naver.com']
    base_urls = "http://search.naver.com/search.naver?where=nexearch&query="
    logging.getLogger('scrapy').propagate = False

    def parse(self, response):
        query_real_rank = '#realrank'
#       print response.css(query_real_rank).extract()
        default_time = int(datetime.datetime.now().timestamp())*10
        titles = response.css('#realrank > li > a::attr(title)').extract()
        urls = response.css('#realrank > li > a::attr(href)').extract()

        results = zip(titles, urls)

        i=1;
        for title, url in results:
            if i <=10:
                print(str(default_time) + "&^%987&^%" + title + "&^%987&^%" + url)
            i+=1
            default_time+=1
            
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(NaverRealRankCrawler)
process.start()
