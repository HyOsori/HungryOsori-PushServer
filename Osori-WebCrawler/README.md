# Osori-WebCrawler
한양대학교 오픈소스동아리에서 만든 크롤러

# Cralwer List
번호 |  크롤링 내용 | Code Link | Github ID
----| ------|---------|-----------|
1 | 한양대학교 컴퓨터전공 공지사항 | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/hanyang_university_cs_notice.py) | [kanak87](https://github.com/kanak87)
2 | 네이버 실시간 검색어 순위 | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/naver_realrank.py) | [kanak87](https://github.com/kanak87)
3 | 남도학숙 주간 식단표  | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/NDHS_Crawler.py) | [CameliaOvO](https://github.com/CameliaOvO)
4 | 디시인사이드 힛갤러리 목록  | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/dcinside_hit_gallery.py) | [jhwon0415](https://github.com/jhwon0415)
5 | 해외축구 일정 결과  | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/FootballGameCrawler.py) | [bees1114](https://github.com/bees1114)
6 | Zangsisi 최신화 | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/zangsisi_recent_manga.py) | [GunjuKo](https://github.com/GunjuKo)
7 | LOL 패치노트 | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/LOLUpdateContent.py) | [seubseub](https://github.com/seubseub)
8 | Steam 세일 | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/steamCrawl.py) | [doomsheart](https://github.com/doomsheart)
9 | 디시인사이드 연극뮤지컬 갤러리 개념글모음 | [Code](https://github.com/HyOsori/Osori-WebCrawler/blob/master/dc_theaterM_gallery.py) | [CameliaOvO](https://github.com/CameliaOvO)

# Contributing
* 크롤러는 python으로 작성해주세요.
* 표준출력을 형식에 맞춰주시면 자동으로 Push가 발송됩니다.
```
고유번호[SEPERATOR]제목[SEPERATOR]링크
```
* 고유번호는 점점 증가해야합니다.
* 크롤러와 settings.json 함께 수정해서 풀리퀘를 날려주세요.

```json
{
...
"dcinside_hit_gallery" : {
    "file_name": "dcinside_hit_gallery.py",
    "crawl_id": "3",
    "crawl_cycle": "60",
    "title": "디시인사이드 힛 갤",
    "desc": "힛갤에 뭐 올라옵니까?",
    "thumbnail": "URL",
    "num_extra_data": "0",
    "separator": "~!@123~!@"
  },
...
}
```

키 | 값 | 설명
---|----|------
dcinside_hit_gallery | Crawler Object | 키는 크롤러의 아이디
file_name | Crawler 파일 이름 | 크롤러 코드
crawl_id | 숫자 | settings.json을 보고, 추가되는 오브젝트의 인덱스 값으로 설정
crawl_cycle | 분 | 크롤러가 실행되는 주기, 단위는 분
title | 타이틀 | 앱에 확인할 수 있는 크롤러 이름
desc | 설명 | 앱에 확인할 수 있는 크롤러 설명
thumbnail | URL | 크롤러 아이콘
num_extra_data | 0-2 | 0 Reserved, 현재 사용되지 않음
seperator | seperator 문자열 | 출력형식에서 고유번호, 제목, 링크를 split하기 위해 사용



# License
MIT Licensed. Copyright (c) Osori 2016.
