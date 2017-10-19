from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://cs.hanyang.ac.kr/board/info_board.php")
source = "http://cs.hanyang.ac.kr/board/info_board.php"
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all('td', {'class' : 'left'})

for result in results:
    text = result.find('a').get_text()
    link = result.find('a')['href']

    if link.find("http") == -1:
        print("Notice : " + text + " / Link : "+ source + link)
    else:
        print("Notice : " + text + " / Link : "+ link)