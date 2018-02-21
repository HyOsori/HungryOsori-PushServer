from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.ndhs.or.kr/2014/sub_community/sub2.php?menuidx=&week=0")
source = "http://www.ndhs.or.kr/2014/sub_community/sub2.php?menuidx=&week=0"
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all('div', {'class': 'meal'})
title = soup.select("div > div > div > div > div > div > table > tbody > tr")
content = soup.select("div > div > div > div > div > div > table > tbody > tr > td")