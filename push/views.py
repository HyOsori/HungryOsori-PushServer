from django.shortcuts import render
import requests

def push_urls(request):
    url = "https://fcm.googleapis.com/fcm/send"

    payload = "data=%7B%20%22notification%22%3A%20%7B%20%20%20%20%20%22title%22%3A%20%22Portugal%20vs.%20Denmark%22%2C%20%20%20%20%20%22text%22%3A%20%225%20to%201%22%20%20%20%7D%2C%20%20%20%22to%22%20%3A%20%22bk3RNwTe3H0%3ACI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...%22%20%7D&to=dYQR2hgIZ50%3AAPA91bE3TSTqsTIwnNmGhNFfQJQfiW7tcKWAozmZuGeXGBBxMdhZc5LTYL4NzsJbOLug_z-8Ia0ts-IQhdsllZmwFwLTETTnHqUeh8otq7Edbz2Wwp-Pu6qZo9Wq3cSdZunfhUmQB4-S"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'authorization': "key=AIzaSyCRyu3phfhkgk87pWSlkBt7MhSEjsMyu4k",
        'cache-control': "no-cache",
        'postman-token': "eace36c8-1927-7140-6d99-3a107350def8"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return render(request, 'blog/post_list.html', {})



# Create your views here.
