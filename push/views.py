import json
import requests 
import subprocess
from django.conf import settings
from pyfcm import FCMNotification
from django.views.decorators.csrf import csrf_exempt
from .models import CrawlData
import datetime
api_list=[]
push_api_and = settings.PUSH_API_AND
push_api_ios = settings.PUSH_API_IOS
api_list.append(push_api_and)
api_list.append(push_api_ios)


@csrf_exempt
def push_urls(token, data_list):
    title = "New Article Arrived"
    message = ""
    tokens = []
    for data in data_list:
        message += data.title + " " + data.urls + "\n"
    for data in token:
        tokens.append(data)
    print(tokens)
    for i in api_list:
        push_service = FCMNotification(api_key=i)
        result = None

        try:
            result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=title,
                                                          message_body=message, data_message={})
        except Exception as e:
            print(e)
            print(str(result))


@csrf_exempt
def crawl_data(request):
    crawl_id = int(request.GET['crawl_id'])
    date_now = datetime.datetime.now()
    with open('Osori-WebCrawler/settings.json') as json_data:
        data = json.load(json_data)

    for key, value in data.items():
        if int(value['crawl_id']) == crawl_id:
            new_data_cnt = 0
            new_data_list = list()
            is_new_exist = False
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
                        is_new_exist = True
                        new_data_cnt += 1
                        new_crawldata = CrawlData(crawler_id=crawler_id, title=sliced_data[1], date=date_now,
                                                  identification_number=int(sliced_data[0]), urls=sliced_data[2])
                        new_crawldata.save()
                        new_data_list.append(new_crawldata)
                    else:
                        break
            except:
                output_list.reverse()
                for data in output_list:
                    sliced_data = data.split(separator)
                    new_crawldata = CrawlData(crawler_id=crawler_id,title=sliced_data[1], date=date_now,
                                              identification_number=int(sliced_data[0]), urls=sliced_data[2])
                    new_crawldata.save()

            if is_new_exist:
                r = requests.post('http://52.78.113.6:8000/subscribers_pushtoken/', data={'crawler_id': 'first crawler'})
                token_data = r.json()
                token_data = token_data['data']
                push_urls(token_data, new_data_list)

    return

