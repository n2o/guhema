# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.list, name='list'),
    url(r'^(?P<slug>[\w-]+)/(?P<type>[\w-]+)/$', views.details, name='details'),
]