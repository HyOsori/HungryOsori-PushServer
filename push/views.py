from django.shortcuts import render
import requests 
import subprocess

#def push_urls(request):
subprocess.call(["python /mnt/c/Users/dooms/HungryOsori-PushServer/push/pushing.py"], shell=True)
subprocess.call(["python /mnt/c/Users/dooms/HungryOsori-PushServer/push/pushingios.py"], shell=True)
#   print(response.text)



# Create your views here.
