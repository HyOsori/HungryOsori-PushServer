from django.db import models
import datetime


class CrawlData(models.Model):
    crawler_id = models.IntegerField()
    title = models.CharField(max_length=300)
    identification_number = models.IntegerField()
    urls = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.datetime.now())
    extra_data_1 = models.CharField(max_length=100, blank=True, default="")
    extra_data_2 = models.CharField(max_length=100, blank=True, default="")
    extra_data_3 = models.CharField(max_length=100, blank=True, default="")
