from django.shortcuts import render
import json
import httplib2
import urllib
import requests 
import subprocess
from django.conf import settings
from pyfcm import FCMNotification
from django.views.decorators.csrf import csrf_exempt
from .models import CrawlData
from django.core import exceptions
from datetime import datetime, timedelta
api_list=[]
push_api_and = settings.PUSH_API_AND
push_api_ios = settings.PUSH_API_IOS
api_list.append(push_api_and)
api_list.append(push_api_ios)


@csrf_exempt
def push_urls(request):
    for i in api_list:
        push_service = FCMNotification(api_key= i)
        result = None
        tokens = []
        title = u"Test!"
        message = u"this is the test push"
        
        #sup = "fOqbayB9yCq3o:APA91bHH4fQu5Bipea_9QEYsnduX0kQ_bMa7FlcaMeP0Jxy0e9KngBaTDwG_ZuSE_TVfjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmR-24jt-8xm5QC53fpepnWQiGXCtt"
#        kkyu = "doQLVh518o8:APA91bFl027SHigp2b1aarCQUfCUaQ-RGOrdU3LYOne-JJlga34bnaeVOnFyW3P9GKwKFqMIFTuHdkKQh4_fGn58DWq9RAlonyAUyFznxw61wgbvnhPZiaCpxoQ3j76EIWMCC_tS037I"
        wohn = "dYQR2hgIZ50:APA91bE3TSTqsTIwnNmGhNFfQJQfiW7tcKWAozmZuGeXGBBxMdhZc5LTYL4NzsJbOLug_z-8Ia0ts-IQhdsllZmwFwLTETTnHqUeh8otq7Edbz2Wwp-Pu6qZo9Wq3cSdZunfhUmQB4-S"
#        yongand = "dMOBkHhz344:APA91bEVoAaHpDJGQ5zIvwpPD_xcKe8Ncl8mP3387h9aKZLLoo8NbJik7lz7Sg6w4lFsUOYwyNxdrKrLkcfXRicoS10JFIhhfPcOHpkjky148SI-yiUCe9M7k9zEn7W-pZtGeL79UM9r"
#        sup = "fOqyB9yCq3o:APA91bHH4fQu5Bipea_9QEYsnduX0kQ_bMa7FlcaMeP0Jxy0e9KngBaTDwG_ZuSE_TVfjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmRjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmR-24jt-8xm5QC53fpepnWQiGXCtt"

        #listname = [kkyu,wohn]
        #for i in listname:

        tokens.append(wohn)
 #       tokens.append(kkyu)
 #       tokens.append(yongand)
 #       tokens.append(sup)
        try:
            result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=title, message_body=message,
                                                                                               data_message={})
        except Exception as e:
            print (e)
            print (str(result))
        data = {
                "result" : 0,
                "message":"success",
                "crawler_id":[
                    
                    ]
                }
#       body = urllib.parse.urlencode(data)
#        h = httplib2.Http()
#       resp, content = h.request("http://52.78.113.6:8000/subscriber_pushtoken/", method="POST", body=body)
    
        data1 = request.POST['title']
        data2 = request.POST['token']
        data3 = request.POST['body']

        print(data1)
        print(data2)
        print(data3)

#    currentDir = subprocess.check_output(["pwd"])
#    currentDir = currentDir[:-1]
#    subprocess.call(["python "+currentDir+"/push/pushing.py"], shell=True)
#    subprocess.call(["python "+currentDir+"/push/pushingios.py"], shell=True)
#   print(response.text)


@csrf_exempt
def crawl_data(request):
    crawl_id = int(request.POST['crawl_id'])
    date_now = datetime.now()
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)

    for key, value in data.items():
        if int(value['crawl_id']) == crawl_id:
            file_name = value['file_name']
            separator = value['separator']
            crawler_id = int(value['crawl_id'])
            output = (subprocess.check_output("python3 Osori-WebCrawler/" + file_name, shell=True)).decode("utf-8")
            output_list = output.splitlines()
            try:
                cur_data = CrawlData.objects.filter(crawler_id=crawler_id).order_by('identification_number')
                last_identification_number = cur_data.last().identification_number
                for data in output_list:
                    sliced_data = data.split(separator)
                    if int(sliced_data[0]) > last_identification_number:
                        new_crawldata = CrawlData(crawler_id=crawler_id, title=sliced_data[1], date=date_now,
                                                  identification_number=int(sliced_data[0]), urls=sliced_data[2])
                        new_crawldata.save()
                    else:
                        break
            except:
                output_list.reverse()
                for data in output_list:
                    sliced_data = data.split(separator)
                    new_crawldata = CrawlData(crawler_id=crawler_id,title=sliced_data[1], date=date_now,
                                              identification_number=int(sliced_data[0]), urls=sliced_data[2])
                    new_crawldata.save()

    return


@csrf_exempt
def testfunc(request):
#    filtering_crawl_id = request.POST['fil_crw_td']
    crawling_cycle = 30 #request.POST['crwl_cycle']
    date_now = datetime.now()   
    last_checked_time = date_now-timedelta(minutes = int(crawling_cycle) )

    data = CrawlData.objects.filter(
            crawler_id = 3,
            date__gte = last_checked_time)
#    data = CrawlData.objects.filter(
#            crawler_id=filtering_crawl_id
#            ).filter( 
#                    (date_now - crwl_cycle)__lte = date)
                    
    for ent in data:
        print(ent.title + "  " +str(ent.date))
    return

