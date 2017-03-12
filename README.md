HungryOsori-PushServer
==========================================
한양대학교 오픈소스 동아리에서 만든 푸시 및 크롤링 서버

기능 
------------------------------------------
* HyOsori/Osori-WebCrawler에 있는 크롤러 파일들 주기적 크롤링
* 변경사항 체크후 Android/iOS 어플에 푸시 알람


크롤링
-------------------------------------------
* Crontab을 이용, 3시간 주기로 크롤링을 한다.
	
- 크롤링 파일 목록

Crawler Id|Crawler Content
---|---
0 |	스팀 세일
1 |	네이버 실시간 랭킹
2 |	남도학숙 식단


변경사항 체크
-------------------------------------------
* url : /crawl_data
* DB에 저장되어 있는 이전 크롤링 데이터와 현재 크롤링 하여 얻은 새로운 데이터(게시물의 제목)를 비교한다.


API 서버와 통신
-------------------------------------------
* url : /push_url
* 변경사항이 발생시 HyOsori/HungryOsori-Server의 API서버에 POST방식으로 Crawler Id 전송
* Request { "crawler_id" : changed_crawler_id}
* Response { "message":"success", "subscriptions": [ { ... }, ] "ErrorCode":0 }

FireBase로 푸시
-------------------------------------------
* url : /push_url
* API와 통신 후 구독자 리스트와 메세지를 FireBase에 전송

Applicaion Type|Code
---|---
Android |	push_service.notify_multiple_devices(registration_ids=tokens, data_message=message_data_android)
iOS |	push_service.notify_multiple_devices(message_title=title_ios, message_body=message_ios,registration_ids=tokens, data_message={})


# License
MIT Licensed. Copyright (c) Osori 2017.