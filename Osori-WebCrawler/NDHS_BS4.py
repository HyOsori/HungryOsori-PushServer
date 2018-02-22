from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ndhs.or.kr/2014/sub_community/sub2.php?menuidx=&week=0")
source = "http://www.ndhs.or.kr/2014/sub_community/sub2.php?menuidx=&week=0"
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all('div', {'class': 'meal'})
title = soup.select("div > div > div > div > div > div > table > tbody > tr > th")
content = soup.select("div > div > div > div > div > div > table > tbody > tr > td")

title_value_list = []
content_value_list = []

for t_val in title:
    title_value_list.append(t_val.text)
for c_val in content:
    content_value_list.append(c_val.text)

for title_index in range(len(title_value_list)):
    print(title_value_list[title_index])
    for content_index in range(3):
        print(content_value_list[title_index*3 + content_index])
