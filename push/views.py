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
import webbrowser

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


@csrf_exempt
def push_urls():
    title_ios = str("구독중인 "+ changed_crawler_id[1] + " 이/가 변경되었습니다!")
    message_ios = str(changed_crawler_id[2])
    message_data_android = {'title': str(changed_crawler_id[1] + " Changed!"),
                    'body': str(changed_crawler_id[2]),
                    'clickurl': str(changed_crawler_id[3])
                    }

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
                # print("and")
                result = push_service.notify_multiple_devices(registration_ids=tokens, data_message=message_data_android)
            elif i == api_list[1]:
                result = push_service.notify_multiple_devices(message_title=title_ios, message_body=message_ios,registration_ids=tokens, data_message={})
            #message_title= title, message_body= message,

        except Exception as e:
            print(e)
            print(str(result))

    tokens.clear()
    return;

@csrf_exempt
def crawl_data(request):
    #Number of Crawlers will be used later
    #update = []

    crawled_data = CrawlData()
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
        #print(output_list)
        #print ("output ::: " + output + " :::::: " + output_list[0])

        title_list = []
        title_list.clear()

        for output_list_ele in output_list :
            listing = output_list_ele.split(separator)
            # print (listing[0])
            title_list.append(listing[crit])
            # print (str(crawler_id) + "add is " + ((listing[crit] + "00000000000")[:10]))

        length_of_list = len(title_list)

        '''if length_of_list > 10 :
            length_of_list = 10
        '''


        for i in range (0, int(length_of_list)) :
            #print("crawler_id : " + str(crawler_id)  + "\ni : " + str(i) + "\n")
            rows = CrawlData.objects.filter(crawler_id=crawler_id).order_by('-date')
            #filter by crawler id & order by descending sequence
            if rows[i] != title_list[i] :
                # print("different !! " + final_list[i])
                data = CrawlData()
                for k in range (0, int(length_of_list)) :
                    # print(str(crawler_id) + " crwadsdsad is and " + str(k) + " is k ::::: " + str(length_of_list) )
                    string_file = title_list[k]

                    #data_base[int(crawler_id)][int(k)] = string_file
                    data.title = string_file



                changed_crawler_id[0] = str(crawler_id)
                changed_crawler_id[1] = value_title
                changed_crawler_id[2] = str("내용중 \"" + title_list[i] + "\"이 변경되었습니다!")
                tmp = (output_list[i].split(separator))
                changed_crawler_id[3] = str(tmp[int(url_index)])   #str(final_list[i][int(url_index)])
                push_urls()
                data.save()
                for j in range(0,int(length_of_list)):
                    print(str(j) + "is :: " + data_base[crawler_id][j] +  "  ")
                title_list.clear()
                break
    return render(request, 'refresh/push_server_page.html')