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
        push_service = FCMNotification(api_key=i)       #get api key in api_list which located in setting.py
        result = None
        tokens = []                                     #define the token array
        title = u"Mario"                                #define title
        message = u"Great Match!"                       #define message adding u before string prevent error

#       wohn = "eKTYlReIRiE:APA91bEzhV7mrxmanXZOzExRyKU-oA1G4UmPal32Kavn0Coh3Q_qIk-w6k7Cgh1eWahBRPan1U4b7jJ-RRW6dlFBrR4yii6mLmYpGDCqEY9KInUvioCcA5qQBSQfK-wziFSCh4pmh143"
        wohn = "dB3mTquf4c0:APA91bG6dr_HBd0PfA3Nt8ILu5GZCCkese1qjbAwqUq8rCybYTuq54BcYPPMfZtUfK0TMfem6k6xj1m66OOIytnweXae-j7D4dR6OgQhgGV2wwsOPmWVaTashQLU_TEeaIUAjmxwtC99"
#listname = [kkyu,wohn]
        #for i in listname:
        wohn2 = "d7X_ODkKsls:APA91bESy9N5iHnArgfeqOpk4n_bhP53zbJK8ZP6rs75bOmIkPDuGcszbA5wUDjs0GsFAYugJjFx41f0LX3f4epWAlN_8dFD9qG_SfWBVLQdVqkbt2J12swmskUhbamDq6pn7SouoDJG"
        tokens.append(wohn)                             #adding wohn token to tokens array
        tokens.append(wohn2)
#       tokens.append(kkyu)
 #       tokens.append(yongand)
 #       tokens.append(sup)
#      data_message = {
#            "Nick": "Mario",
#            "body": "great match!",
#            "Room": "PortugalVSDenmark"
#        }
        message_data = {
            'title':'Steam',
            'clickurl':'https://github.com/hyosori'
        }
#        title = str(request.POST[data_message["Nick"]])
#        body = str(request.POST[data_message["body"]])

#        data1 = request.POST['title']
#        data3 = request.POST['body']

#        print(data1)
#        print(data3)
        try:
            result = push_service.notify_multiple_devices(registration_ids=tokens,data_message = message_data)

        #    result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=title,
        #                                                 message_body=message, data_message={})
        except Exception as e:
            print (e)
            print (str(result))
        data = {                                        #data form would be used later...
                "result" : 0,
                "message":"success",
                "crawler_id":[

                    ]
                }

#       body = urllib.parse.urlencode(data)
#        h = httplib2.Http()
#       resp, content = h.request("http://52.78.113.6:8000/subscriber_pushtoken/", method="POST", body=body)
    


#    currentDir = subprocess.check_output(["pwd"])
#    currentDir = currentDir[:-1]
#    subprocess.call(["python "+currentDir+"/push/pushing.py"], shell=True)
#    subprocess.call(["python "+currentDir+"/push/pushingios.py"], shell=True)
#   print(response.text)

@csrf_exempt
def crawl_data(request):
    crawl_id = int(request.POST['crawl_id'])                    #when receive the post and get crwal_id
    date_now = datetime.now()
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)                             #save the json_data in data

    for key, value in data.items():                             #get key and value in data class
        if int(value['crawl_id']) == crawl_id:                  #find the crawl_id
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
                    else:
                        break
            except:             #when the display of board is up to down,
                output_list.reverse()       #reverse the order
                for data in output_list:   #data is parameter in output_list
                    sliced_data = data.split(separator)                 #CrawlData from model
                    new_crawldata = CrawlData(crawler_id=crawler_id,title=sliced_data[1], date=date_now,
                                              identification_number=int(sliced_data[0]), urls=sliced_data[2])
                    new_crawldata.save()

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

