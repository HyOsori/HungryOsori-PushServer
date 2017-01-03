import scrapy

from scrapy.crawler import CrawlerProcess


class SteamSpider(scrapy.Spider):
    name = 'steam sale off'
    start_urls = ['http://store.steampowered.com/search/?specials=1&os=win#sort_by=_ASC&specials=1&page=1']

    def parse(self, response):
        titles = response.css(
            '#search_result_container > div > a > div:nth-child(2) > div:nth-child(1) > span::text').extract()
        saleOff = response.css(
            '#search_result_container > div:nth-child(2) > a > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow>span::text').extract()
        #defaultPrice = response.css('#search_result_container > div:nth-child(2) > a > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow>span>strike::text').extract()

        refs = response.css('#search_result_container > div:nth-child(2) > a::attr(href)').extract()
        results = zip(titles, refs, saleOff)
        for title, saleOff, defaultPrice in results:
            print str(number) + "~!@123~!@" + title + "~!@123~!@" + self.base_urls + ref


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SteamSpider)
process.start()
