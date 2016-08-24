from django.shortcuts import render
import requests

def push_urls(request):
    url = "https://fcm.googleapis.com/fcm/send"

    payload = "data=%7B%20%22multicast_id%22%3A%20216%2C%20%20%20%22success%22%3A%203%2C%20%20%20%22failure%22%3A%203%2C%20%20%20%22canonical_ids%22%3A%201%2C%20%20%20%22results%22%3A%20%5B%20%20%20%20%20%7B%20%22message_id%22%3A%20%221%3A0408%22%20%7D%2C%20%20%20%20%20%7B%20%22error%22%3A%20%22Unavailable%22%20%7D%2C%20%20%20%20%20%7B%20%22error%22%3A%20%22InvalidRegistration%22%20%7D%2C%20%20%20%20%20%7B%20%22message_id%22%3A%20%221%3A1516%22%20%7D%2C%20%20%20%20%20%7B%20%22message_id%22%3A%20%221%3A2342%22%2C%20%22registration_id%22%3A%20%2232%22%20%7D%2C%20%20%20%20%20%7B%20%22error%22%3A%20%22NotRegistered%22%7D%20%20%20%5D%20%7D&to=eO6WaMzsDiY%3AAPA91bFnzMgzFpXUi-Ntr-YDrtH6iDX5xeQOxQ7oJDL1R2rdDLAYu2EbIqMM77IJFBAH7WP9xx_g8BAWoZaDKPTsdRLhneMdYqwnpIpUncJTzNf03PLH841WwGsEpYQs_V-tVo6fDtEe" 
    headers = {
            'content-type': "application/x-www-form-urlencoded",
            'authorization': "key=AIzaSyCRyu3phfhkgk87pWSlkBt7MhSEjsMyu4k",
            'cache-control': "no-cache",
            'postman-token': "1f42827b-121f-49a4-f6a4-57ede577fed1"
}


    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    return render(request, 'blog/post_list.html', {})



# Create your views here.
