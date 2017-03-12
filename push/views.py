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
from push.models import CrawlData
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
api_request_url = 'http://52.78.113.6:8000/subscribers_pushtoken/'


@csrf_exempt
def push_urls(crawler_id, crawler_name, changed_line, url_link ):
    #make push message for ios
    title_ios = str("구독중인 "+ crawler_name + " 이/가 변경되었습니다!")
    message_ios = str(changed_line)

    #make push message for android
    message_data_android = {'title': str(crawler_name + " Changed!"),
                    'body': str(changed_line),
                    'clickurl': str(url_link)
                    }

    #shoot the crawler id to API server and receive the subscribe user as json type
    payload = {'crawler_id': crawler_id}
    received_json = requests.post(api_request_url, data=payload)

    #parse the json user data
    token_receive_data = received_json.json()
    for k in token_receive_data['data']:
        tokens.append(k['push_token'])


    for i in api_list:
        push_service = FCMNotification(api_key=i)
        result = None
        try:
            if i == api_list[0]:    #which means push to android
                result = push_service.notify_multiple_devices(registration_ids=tokens, data_message=message_data_android)
            elif i == api_list[1]:  #which means push to ios
                result = push_service.notify_multiple_devices(message_title=title_ios, message_body=message_ios,registration_ids=tokens, data_message={})

        except Exception as e:
            print(e)
            print(str(result))

    tokens.clear()
    return;

@csrf_exempt
def crawl_data(request):
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)                             #save the json_data in data

    for key, value in data.items():         #current, 170311, We only available in crawler 0, 1, 2 because of error in other crawler file

        file_name = value['file_name']
        separator = value['separator']
        crawler_id = int(value['crawl_id'])
        value_title = value['title']
        url_index = value['url_index']
        criteria = int(value['criteria'])

        output = (subprocess.check_output("python3 Osori-WebCrawler/" + file_name, shell=True)).decode("utf-8") #crawl the file
        crawling_result_list = output.splitlines()                   #split its data by word-break

        title_list = []

        for crawling_element in crawling_result_list :
            crawl_result_info = crawling_element.split(separator)
            title_list.append(crawl_result_info[criteria])

        length_of_list = len(title_list)


        for i in range (0, int(length_of_list)) :
            rows = CrawlData.objects.filter(crawler_id=crawler_id).order_by('-date')
            if rows[(length_of_list - i - 1)].title != title_list[i] :

                for k in range (0, int(length_of_list)) :
                    string_file = title_list[k]
                    modeldata = CrawlData()
                    modeldata.crawler_id = crawler_id
                    modeldata.title = string_file
                    modeldata.urls = url_index
                    modeldata.save()


                changed_url_link = (crawling_result_list[i].split(separator))
                push_urls(str(crawler_id)
                                 , value_title
                                 , str("내용중 \"" + title_list[i] + "\"이 변경되었습니다!")
                                 , str(changed_url_link[int(url_index)]))
                title_list.clear()
                break
    return render(request, 'refresh/push_server_page.html')


@csrf_exempt
def create_data(request):   #This function is made for create initial data.
                            #Because if there's no data in DB, we retrieve null value, which can cause null array.
                            #Empty array can make the range out error.

    with open('Osori-WebCrawler/settings.json') as json_data:
        setting_data = json.load(json_data)                             #save the json_data in data


    for key, value in setting_data.items():         #current, 170311, We only available in crawler 0, 1, 2

        file_name = value['file_name']
        separator = value['separator']
        crawler_id = int(value['crawl_id'])
        url_index = value['url_index']
        criteria = int(value['criteria'])

        output = (subprocess.check_output("python3 Osori-WebCrawler/" + file_name, shell=True)).decode("utf-8") #crawl the file
        crawling_result_list = output.splitlines()                   #split its data by enter

        title_list = []

        for crawling_element in crawling_result_list :
            crawl_result_info = crawling_element.split(separator)
            title_list.append(crawl_result_info[criteria])

        length_of_list = len(title_list)

        for i in range(0, int(length_of_list)):
                modeldata = CrawlData()
                string_file = title_list[i]
                modeldata.crawler_id = crawler_id
                modeldata.title = string_file
                modeldata.urls = url_index
                modeldata.save()

    return render(request, 'refresh/push_server_page.html')

