from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.push_urls, name='push_urls'),
            url(r'test', views.crawl_data, name='crawl_data'),
            url(r'send', views.API_send, name='API_send'),
            url(r'test_request', views.test_request, name='test_request'),
            url(r'hello_world', views.hello_world, name= 'hello_world')
]
