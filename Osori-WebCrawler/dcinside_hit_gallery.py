import scrapy
from scrapy.crawler import CrawlerProcess
import logging


class DCInsideHitGalleryCrawler(scrapy.Spider):
    name = 'DC Inside HitGallery - crawler'
    start_urls = ['http://gall.dcinside.com/board/lists/?id=hit&page=1']
    base_urls = 'http://gall.dcinside.com'
    logging.getLogger('scrapy').propagate = False

    def parse(self, response):

        query_notice_title = '.list_thead > tr > td:nth-child(2) > a::text'
        query_notice_number = '.list_thead > tr > td:nth-child(1)::text'
        query_notice_ref = '.list_thead > tr > td:nth-child(2) > a:nth-child(1)::attr(href)'
        numbers = [int(text) for text in response.css(query_notice_number).extract() if text.isdigit()]
        titles = response.css(query_notice_title).extract()
        refs = (response.css(query_notice_ref).extract())[2:]
        pairs = zip(numbers, titles, refs)
        for number, pair, ref in pairs:
            print(str(number) + "~!@123~!@" + pair + "~!@123~!@" + self.base_urls + ref)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(DCInsideHitGalleryCrawler)
process.start()
