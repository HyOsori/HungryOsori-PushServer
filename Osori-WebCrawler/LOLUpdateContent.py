import scrapy
import datetime, time
from scrapy.crawler import CrawlerProcess

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

_seperator_ = "~!@123~!@"


class LOLUpdateContent(scrapy.Spider):
    name = 'LOL Update Content'
    start_urls = ['http://www.leagueoflegends.co.kr/?m=news&cate=update']

    def parse(self, response):
        dates = response.css(
            'body > div.section-wrapper.section-wrapper-primary > div > div > div > div.left-contents > div:nth-child(2) > div > table > tbody > tr > td:nth-child(2)::text').extract()
        unique_ids = map(lambda value: int(time.mktime(datetime.datetime.strptime(value, "%Y-%m-%d").timetuple())), dates)
        titles = response.css("td.tleft a::text").extract()
        urls = response.css("td.tleft a::attr(href)").extract()

        print 'League of Legends Update Note'

        final = zip(unique_ids, titles, urls)

        for id, title, url in final:
            print str(id) + _seperator_ + title + _seperator_ + 'http://www.leagueoflegends.co.kr' + url


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(LOLUpdateContent)
process.start()
