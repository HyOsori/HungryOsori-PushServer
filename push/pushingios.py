# -*- coding: utf-8 -*-

from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AIzaSyBEVkJRz7HazHJq_u8NmQP5ZLJikf1lEbM")

result = None
tokens = []
title = u"Test!"
message = u"this is the test push"

sup = "fOqyB9yCq3o:APA91bHH4fQu5Bipea_9QEYsnduX0kQ_bMa7FlcaMeP0Jxy0e9KngBaTDwG_ZuSE_TVfjn_GmA5FoSeuaHrD9KN6vRNYBtmaCbAYPK8N90tF0BBmR-24jt-8xm5QC53fpepnWQiGXCtt"
kkyu = "doQLVh518o8:APA91bFl027SHigp2b1aarCQUfCUaQ-RGOrdU3LYOne-JJlga34bnaeVOnFyW3P9GKwKFqMIFTuHdkKQh4_fGn58DWq9RAlonyAUyFznxw61wgbvnhPZiaCpxoQ3j76EIWMCC_tS037I"
wohn = "dYQR2hgIZ50:APA91bE3TSTqsTIwnNmGhNFfQJQfiW7tcKWAozmZuGeXGBBxMdhZc5LTYL4NzsJbOLug_z-8Ia0ts-IQhdsllZmwFwLTETTnHqUeh8otq7Edbz2Wwp-Pu6qZo9Wq3cSdZunfhUmQB4-S"
yongand = "dMOBkHhz344:APA91bEVoAaHpDJGQ5zIvwpPD_xcKe8Ncl8mP3387h9aKZLLoo8NbJik7lz7Sg6w4lFsUOYwyNxdrKrLkcfXRicoS10JFIhhfPcOHpkjky148SI-yiUCe9M7k9zEn7W-pZtGeL79UM9r"


tokens.append(sup)
#tokens.append()
#tokens.append()
try:
            result = push_service.notify_multiple_devices(registration_ids=tokens, message_title=title, message_body=message,
                                                                                      data_message={})
except Exception as e:
            print e

            print str(result)
