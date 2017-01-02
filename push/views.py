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
from rest_framework.response import Response

api_list=[]
push_api_and = settings.PUSH_API_AND
push_api_ios = settings.PUSH_API_IOS
api_list.append(push_api_and)
api_list.append(push_api_ios)


@csrf_exempt
def push_urls(token):
    title = "IOS NOTIFICATION"
    message = "IOS"
    tokens = []
    fuck = 'cKYp-sSJMuA:APA91bF9Jtlf2KsPknooy--OcJr0S9Qm9ebjc3novTLMZI08WH7_2F6zklJzHnuaULuuAo7sw-g9Ht6_TtRkOxPa9ZDRLQ5NtR6jCGOhUZAKbax0dHYfRSsyEL9LRL5CMHpkF7SxRMtc'
#    sub = 'e3zQZA9Iqks:APA91bGsYV3VFDZtogzTQ_cH0rObpsvSVdHvj_UtRCjm_CWFEjDHDd7cvB31TWS6_CaapoQH6r1C3FPi3aVQrdzmFDNSKnS_v5LNfLuGwx6iL-HgUYvJCE0KMHeb6bstuzkiu5Nvjlmf'
#    fuck2 = 'dXw-spzO5Qc:APA91bFdpFt48hEAk7lBQV4A-vOmFEuWibKXaHdis7gmldCY4uVwbDZfxZ23yBzyRKvgsscV6tVhZL-wTXT5A08LCxxfGhuBn8tz2Crifc7eMaRbmJvWJvw9z4uDdUdIp_y2Jsdr5lQS'
    tokens.append(fuck)
 #   tokens.append(sub)
 #   tokens.append(fuck2)
    message_data = {'title': 'Android Data Reboot',
                        'body': 'Android',
                        'clickurl' : 'http://www.daum.net'
                    }
#    for data in dat    a_list:
#        message += data.title + " " + data.urls + "\n"
#    for data in token:
#        tokens.append(data)
#    print(tokens)
    for i in api_list:
        push_service = FCMNotification(api_key=i)
        result = None
        try:
            if i == api_list[0]:
                result = push_service.notify_multiple_devices(registration_ids=tokens, data_message=message_data)
            elif i == api_list[1]:
                result = push_service.notify_multiple_devices(message_title=title, message_body=message,registration_ids=tokens, data_message={})
            #message_title= title, message_body= message,
        except Exception as e:
            print(e)
            print(str(result))

@csrf_exempt
def test_request():
    URL = "52.78.113.6:8000/subscribers_pushtoken/"
    data = {'crawler_id' : '2'}
    req = urllib.Request()
    result = Response(URL, data)




@csrf_exempt
def crawl_data():
    #Number of Crawlers will be used later
    update = []

    date_now = datetime.now()
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)                             #save the json_data in data

    for key, value in data.items():
        update.append(0)
        #get key and value in data class
        #find the crawl_id
        file_name = value['file_name']                      #value is dictionary type, so it access by its index
        separator = value['separator']
        crawler_id = int(value['crawl_id'])
        output = (subprocess.check_output("python3 Osori-WebCrawler/" + file_name, shell=True)).decode("utf-8") #crawl the file
        output_list = output.splitlines()                   #split its data by word-break
        try:
            cur_data = CrawlData.objects.filter(crawler_id=crawler_id).order_by('identification_number') #filtering data by crawler_id and ordering identification_number
            last_identification_number = cur_data.last().identification_number  #saving last identification number
            for data in output_list:            #list of data in output list which splited by spaces
                sliced_data = data.split(separator)     #seperating by seperator value received in data.items()
            if int(sliced_data[0]) > last_identification_number:    #which means the new post is written,
                new_crawldata = CrawlData(crawler_id=crawler_id, title=sliced_data[1], date=date_now,   #switch the data
                                          identification_number=int(sliced_data[0]), urls=sliced_data[2])
                new_crawldata.save()
                update[crawler_id] = 1
            else:
                break
        except:             #when the display of board is up to down,
            output_list.reverse()       #reverse the order
            for data in output_list:   #data is parameter in output_list
                sliced_data = data.split(separator)                 #CrawlData from model
                new_crawldata = CrawlData(crawler_id=crawler_id,title=sliced_data[1], date=date_now,
                                          identification_number=int(sliced_data[0]), urls=sliced_data[2])

                new_crawldata.save()
                update[crawler_id] = 1

    return update



@csrf_exempt
def send(update,num):
    if(update[num-1]==1):
        data = {'crawler_id' : num}
        return Response(data)
    else:
        return

@csrf_exempt
def API_send():
    update = crawl_data()

    for crawl_id in update:
        send(update,crawl_id + 1)

    return

@csrf_exempt
def testfunc(request):
#    filtering_crawl_id = request.POST['fil_crw_td']
    crawling_cycle = 0 #request.POST['crwl_cycle']          #0 means crawl repeatly
    date_now = datetime.now()                               #save data time now
    last_checked_time = date_now-timedelta(minutes = int(crawling_cycle))  #

    data = CrawlData.objects.all()      #crawl data from model, and go into object and all,
#    filter(
#            crawler_id = 3,
#            date__gte = last_checked_time)
#    data = CrawlData.objects.filter(
#            crawler_id=filtering_crawl_id
#            ).filter( 
#                    (date_now - crwl_cycle)__lte = date)
                    
    for ent in data:                    #
        print(ent.title + "  " + str(ent.date))
    return

