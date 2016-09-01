from django.shortcuts import render
import requests 
import subprocess
from django.conf import settings
from pyfcm import FCMNotification
api_list=[]
push_api_and = settings.PUSH_API_AND
push_api_ios = settings.PUSH_API_IOS
api_list.append(push_api_and)
api_list.append(push_api_ios)


def push_urls(request):
    for i in api_list:
        push_service = FCMNotification(api_key= i)
        result = None
        tokens = []
        title = u"Test!"
        message = u"this is the test push"
        
        #sup = "fOqyB9yCq3o:APA91bHH4fQu5Bipea_9QEYsnduX0kQ_bMa7FlcaMeP0Jxy0e9KngBaTDwG_ZuSE_TVfjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmR-24jt-8xm5QC53fpepnWQiGXCtt"
        kkyu = "doQLVh518o8:APA91bFl027SHigp2b1aarCQUfCUaQ-RGOrdU3LYOne-JJlga34bnaeVOnFyW3P9GKwKFqMIFTuHdkKQh4_fGn58DWq9RAlonyAUyFznxw61wgbvnhPZiaCpxoQ3j76EIWMCC_tS037I"
        wohn = "dYQR2hgIZ50:APA91bE3TSTqsTIwnNmGhNFfQJQfiW7tcKWAozmZuGeXGBBxMdhZc5LTYL4NzsJbOLug_z-8Ia0ts-IQhdsllZmwFwLTETTnHqUeh8otq7Edbz2Wwp-Pu6qZo9Wq3cSdZunfhUmQB4-S"
        yongand = "dMOBkHhz344:APA91bEVoAaHpDJGQ5zIvwpPD_xcKe8Ncl8mP3387h9aKZLLoo8NbJik7lz7Sg6w4lFsUOYwyNxdrKrLkcfXRicoS10JFIhhfPcOHpkjky148SI-yiUCe9M7k9zEn7W-pZtGeL79UM9r"
        sup = "fOqyB9yCq3o:APA91bHH4fQu5Bipea_9QEYsnduX0kQ_bMa7FlcaMeP0Jxy0e9KngBaTDwG_ZuSE_TVfjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmRjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmR-24jt-8xm5QC53fpepnWQiGXCtt"

        #listname = [kkyu,wohn]
        #for i in listname:

        tokens.append(wohn)
        tokens.append(kkyu)
        tokens.append(yongand)
        tokens.append(sup)
        try:
            result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=title, message_body=message,
                                                                                              data_message={})
        except Exception as e:
            print e
            print str(result)
    
    
    
    
#    currentDir = subprocess.check_output(["pwd"])
#    currentDir = currentDir[:-1]
#    subprocess.call(["python "+currentDir+"/push/pushing.py"], shell=True)
#    subprocess.call(["python "+currentDir+"/push/pushingios.py"], shell=True)
#   print(response.text)



# Create your views here.
