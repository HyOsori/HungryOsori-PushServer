from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.push_urls, name='push_urls'),
            url(r'test', views.crawl_data, name='crawl_data'),
            url(r'send', views.API_send, name='API_send'),
            url(r'hello_1', views.hello_1, name='hello_1'),
            url(r'hello_2', views.hello_2, name='hello_2')
]
