#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://store.steampowered.com/search/?specials=1&os=win#sort_by=_ASC&specials=1&page=1")
soup = BeautifulSoup(html, "html.parser")
box = soup.find_all(id='search_result_container')
title = box[0].find_all(class_='title')
titles = []
for t in title:
    titles.append(t.text)
urls = []
for a in box[0].find_all('a', href=True):
    urls.append(a['href'])

salepers = box[0].find_all(class_='col search_discount responsive_secondrow')
sales = []
for s in salepers:
    try:
        sales.append(s.find_all('span')[0].text)
    except:
        sales.append("0%")

prices = []
for p in box[0].find_all(class_='col search_price discounted responsive_secondrow'):
    prices.append(p.find_all('span')[0].text[2:])

discounted = []
for p in box[0].find_all(class_='col search_price discounted responsive_secondrow'):
    discounted.append(p.contents[3][2:-7])

result = list(zip(titles, urls, sales, prices, discounted))

print(result)

# class SteamSpider(scrapy.Spider):
#     name = 'steam sale off'
#     start_urls = ['http://store.steampowered.com/search/?specials=1&os=win#sort_by=_ASC&specials=1&page=1']
#
#     logging.getLogger('scrapy').propagate = False
#
#     def parse(self, response):
#         titles = response.css(
#             '#search_result_container > div > a > div:nth-child(2) > div:nth-child(1) > span::text').extract()
#         saleOff = response.css(
#             '#search_result_container > div:nth-child(2) > a > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow>span::text').extract()
#         #defaultPrice = response.css('#search_result_container > div:nth-child(2) > a > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow>span>strike::text').extract()
#
#         refs = response.css('#search_result_container > div:nth-child(2) > a::attr(href)').extract()
#         results = zip(titles, refs, saleOff)
#         for title, saleOff, defaultPrice in results:
#             #print (title)
#             print (title + " discount " + defaultPrice  + " &^%987&^%" + saleOff)
# #            print (str('1') + "~!@123~!@" + title + "~!@123~!@" + self.base_urls + refs)


