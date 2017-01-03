# -*- coding: utf-8 -*-
import scrapy
import datetime, time
from scrapy.crawler import CrawlerProcess

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

_seperator_ = "~!@123~!@"


class FootballGameCrawler(scrapy.Spider):
    name = 'FootballGameCrawler'
    start_urls = ['http://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%ED%95%B4%EC%99%B8%EC%B6%95%EA%B5%AC+%EA%B2%BD%EA%B8%B0+%EA%B2%B0%EA%B3%BC&tltm=1']

    def to_id(self, value):
        hour, minute = value.split(':')
        today = datetime.datetime.today()
        today.replace(hour=int(hour), minute=int(minute), microsecond=0)
        return str(time.mktime(today.timetuple()))

    def parse(self, response):
        times = response.css('#testTbl > table > tbody > tr > td.cont1 > em::text').extract()
        leagues = response.css('#testTbl > table > tbody > tr > td.cont1 > span > a::text').extract()
        team1s = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.home > span::text').extract()
        score1s = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.home > em::text').extract()
        score2s = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.away > em::text').extract()
        team2s = response.css('#testTbl > table > tbody > tr > td.cont2 > a > div > div.away > span::text').extract()

        unique_ids = map(self.to_id, times)
        table = zip(unique_ids, leagues, team1s, score1s, score2s, team2s)

        for id, league, team1, score1, score2, team2 in table:
            title = league + ' '+ team1 + ' ' + score1 + ' : ' + score2 + ' ' + team2
            print id + _seperator_ + title + _seperator_ + self.start_urls[0]


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(FootballGameCrawler)
process.start()
