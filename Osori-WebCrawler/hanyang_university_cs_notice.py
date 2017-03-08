import scrapy
from scrapy.crawler import CrawlerProcess
import logging
import datetime

class CSHanyangCrawler(scrapy.Spider):
    name = "cs.hanyang - crawler"
    allowed_domains = ["cs.hanyang.ac.kr"]
    start_urls = ["http://cs.hanyang.ac.kr/board/info_board.php"]
    base_urls = "http://cs.hanyang.ac.kr"
    logging.getLogger('scrapy').propagate = False

    def parse(self, response):
        query_notice_urls = "#content_in > div > table > tr > td.left > a::attr(href)"
        query_notice_title = "#content_in > div > table > tr > td.left > a::text"

        default_time = int(datetime.datetime.now().timestamp()) * 10

        urls = response.css(query_notice_urls).extract()
        texts = response.css(query_notice_title).extract()

        pairs = zip(texts,urls)

        for title,url in pairs:
            print(title + "&^%987&^%" + self.base_urls + url + "&subkind=&offset=0")

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(CSHanyangCrawler)
process.start()