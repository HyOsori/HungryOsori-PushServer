import scrapy
import datetime, time
from scrapy.crawler import CrawlerProcess

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

_seperator_ = "~!@123~!@"


class ZangsisiCrawler(scrapy.Spider):
    name = 'zangsisi'
    start_urls = ['http://zangsisi.net/']

    def parse(self, response):
        query_date = "#recent-manga > div > li > div.date::text"
        query_contents = "#recent-manga > div > li > div.contents > a::text"
        query_urls = "#recent-manga > div > li:nth-child(1) > div.contents > a::attr(href)"

        dates = response.css(query_date).extract()
        unique_ids = map(lambda value: int(time.mktime(datetime.datetime.strptime('2016-'+(value.replace('/','-')), "%Y-%m-%d").timetuple())), dates)
        contents = response.css(query_contents).extract()
        urls = response.css(query_urls).extract()

        results = zip(unique_ids, contents, urls)

        for id, content, url in results:
            print str(id) + _seperator_ + content + _seperator_ + url


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(ZangsisiCrawler)
process.start()
