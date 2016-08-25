from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.push_urls, name='push_urls'),
]
