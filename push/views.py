from django.shortcuts import render
import requests 
import subprocess

def push_urls(request):
    currentDir = subprocess.check_output(["pwd"])
    currentDir = currentDir[:-1] #deleting the '\n' word at the end that printed by defalut
    subprocess.call(["python "+currentDir+"/push/pushing.py"], shell=True)
    subprocess.call(["python "+currentDir+"/push/pushingios.py"], shell=True)
#   print(response.text)



# Create your views here.
