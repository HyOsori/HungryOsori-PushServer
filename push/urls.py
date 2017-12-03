from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'push_urls', views.push_urls, name='push_urls'),
            url(r'crawl_data', views.crawl_data, name='crawl_data'),
            url(r'create_data', views.create_data, name='create_data'),
            url(r'push_test_ios', views.push_test_ios, name='push_test_ios'),
]
