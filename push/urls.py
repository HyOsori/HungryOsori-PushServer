from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.push_urls, name='push_urls'),
            url(r'test', views.crawl_data, name='crawl_data'),
            url(r'createdata', views.create_data, name='create_data'),
]
