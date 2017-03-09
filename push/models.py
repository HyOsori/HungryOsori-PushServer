from django.db import models
import datetime


class CrawlData(models.Model):
    crawler_id = models.IntegerField()
    title = models.CharField(max_length=300)
    urls = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
