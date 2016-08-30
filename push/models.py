from django.db import models

# Create your models here.

class CrawlingResult(models.Model):
    post_id = models.IntegerField()
    post_title = models.CharField(max_length=100)
    post_link = models.CharField(max_length=1000)
    crawler_id = models.IntegerField()


    

