from django.shortcuts import render
import sqlite3 as sqlite
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
tokens = []
changed_crawler_id = ['0', 'crawler_name', 'changed_line', 'link_urls']
data_base = [['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10'],
             ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10'],
             ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']]
db_created = 0


@csrf_exempt
def push_urls(void):
    title_ios = str(changed_crawler_id[1] + " Changed!")
    message_ios = str(changed_crawler_id[2])
    message_data_android = {'title': str(changed_crawler_id[1] + " Changed!"),
                    'body': str(changed_crawler_id[2]),
                    'clickurl': str(changed_crawler_id[3])
                    }

    print("/////////// urls is " + changed_crawler_id[3])

    api_request_url = 'http://52.78.113.6:8000/subscribers_pushtoken/'
    payload = {'crawler_id': changed_crawler_id[0]}
    r = requests.post(api_request_url, data=payload)
    token_receive_data = r.json()
    for k in token_receive_data['data']:
        tokens.append(k['push_token'])


    for i in api_list:
        push_service = FCMNotification(api_key=i)
        result = None
        try:
            if i == api_list[0]:
                print("and")
                result = push_service.notify_multiple_devices(registration_ids=tokens, data_message=message_data_android)
            elif i == api_list[1]:
                result = push_service.notify_multiple_devices(message_title=title_ios, message_body=message_ios,registration_ids=tokens, data_message={})
            #message_title= title, message_body= message,

        except Exception as e:
            print(e)
            print(str(result))

    tokens.clear()


@csrf_exempt
def test_time(void) :
    date_now = datetime.now()

@csrf_exempt
def teste_crawl(void) :

    date_now = datetime.now()
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)





@csrf_exempt
def crawl_data(void):
    #Number of Crawlers will be used later
    #update = []

    date_now = datetime.now()
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)                             #save the json_data in data

    for key, value in data.items():         #current, 170103, We only available in crawler 1, 2 because of error in crawler file
        #update.append(0)
        #get key and value in data class
        #find the crawl_id
        file_name = value['file_name']                      #value is dictionary type, so it access by its index
        separator = value['separator']
        crawler_id = int(value['crawl_id'])
        value_title = value['title']
        url_index = value['url_index']
        crit = int(value['criteria'])
        # print(file_name + " " + separator + " " + str(crawler_id) + " " + value_title + " " + str(crit))
        #print ("criteria s :::: " + str(crit))
        #print (file_name + " :::: " + separator + " :::: " + str(crawler_id))
        output = (subprocess.check_output("python3 Osori-WebCrawler/" + file_name, shell=True)).decode("utf-8") #crawl the file
        output_list = output.splitlines()                   #split its data by word-break
        print(output_list)
        #print ("output ::: " + output + " :::::: " + output_list[0])
        final_list = []


        final_list.clear()

        for output_list_ele in output_list :
            listing = output_list_ele.split(separator)
            print (listing[0])
            final_list.append(listing[crit])
            # print (str(crawler_id) + "add is " + ((listing[crit] + "00000000000")[:10]))

        length_of_list = len(final_list)

        # for ele in data_base[crawler_id]:
        #     print (str(ele))




        # cur_data = CrawlData.objects.filter(crawler_id=crawler_id).order_by('identification_number') #filtering data by crawler_id and ordering identification_number
        # last_identification_number = cur_data.last().identification_number  #saving last identification number
        # for data in output_list:            #list of data in output list which splited by spaces
        #     sliced_data = data.split(separator)     #seperating by seperator value received in data.items()
        # if int(sliced_data[0]) > last_identification_number:    #which means the new post is written,
        #     new_crawldata = CrawlData(crawler_id=crawler_id, title=sliced_data[1], date=date_now,   #switch the data
        #                                   identification_number=int(sliced_data[0]), urls=sliced_data[2])
        #     new_crawldata.save()
        # else:
        #     break



        for i in range (0, int(length_of_list)) :
            print("crawler_id : " + str(crawler_id)  + "\ni : " + str(i) + "\n")
            if data_base[crawler_id][i] != final_list[i] :
                print("different !! " + final_list[i])
                for k in range (0, int(length_of_list)) :
                    print(str(crawler_id) + " crwadsdsad is and " + str(k) + " is k ::::: " + str(length_of_list) )
                    string_file = final_list[k]

                    data_base[int(crawler_id)][int(k)] = string_file



                changed_crawler_id[0] = str(crawler_id)
                changed_crawler_id[1] = value_title
                changed_crawler_id[2] = str("내용중 \"" + final_list[i] + "\"이 변경되었습니다!")
                tmp = (output_list[i].split(separator))
                changed_crawler_id[3] = str(tmp[int(url_index)])   #str(final_list[i][int(url_index)])
                push_urls(void)
                for j in range(0,int(length_of_list)):
                    print(str(j) + "is :: " + data_base[crawler_id][j] +  "  ")
                final_list.clear()
                break
    return

'''
@csrf_exempt
def db_creating(void):
    if db_created == 1:
        return 0
    elif db_created == 0:
        def __init
'''


'''
            cur_data = CrawlData.objects.filter(crawler_id=crawler_id).order_by('identification_number') #filtering data by crawler_id and ordering identification_number
            print("cur_data :: " + cur_data)
            last_identification_number = cur_data.last().identification_number  #saving last identification number
            print("last_idem :: " + last_identification_number)
            for data in output_list:            #list of data in output list which splited by spaces
                sliced_data = data.split(separator)     #seperating by seperator value received in data.items()
                print("sliced_data :: " + sliced_data)
            if int(sliced_data[0]) > last_identification_number:    #which means the new post is written,
                new_crawldata = CrawlData(crawler_id=crawler_id, title=sliced_data[1], date=date_now,   #switch the data
                                          identification_number=int(sliced_data[0]), urls=sliced_data[2])
                new_crawldata.save()
                update[crawler_id] = 1
            else:
                break
                '''
'''        except:             #when the display of board is up to down,
            output_list.reverse()       #reverse the order
            for data in output_list:   #data is parameter in output_list
                sliced_data = data.split(separator)                 #CrawlData from model
                new_crawldata = CrawlData(crawler_id=crawler_id,title=sliced_data[1], date=date_now,
                                          identification_number=int(sliced_data[0]), urls=sliced_data[2])

                new_crawldata.save()
             #   update[crawler_id] = 1


    #return update

'''
@csrf_exempt
def hello_1(void):
    print ("hello_1 is called!")
    hello_2(void)

@csrf_exempt
def hello_2(void):
    print ("hello_2 is called!")

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

