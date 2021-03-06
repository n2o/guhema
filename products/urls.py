# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lochsagen/empfehlung$', views.holesawAdvice, name='holesaw_advice'),
    url(r'^(?P<slug>[\w-]+)/$', views.list, name='list'),
    url(r'^(?P<slug>[\w-]+)/details$', views.product_details, name='product_details'),
    url(r'^(?P<slug>[\w-]+)/empfehlungen$', views.product_advices, name='advices'),
    url(r'^(?P<slug>[\w-]+)/(?P<id>[0-9]+)/$', views.details_by_id, name='details_by_id'),
    url(r'^(?P<slug>[\w-]+)/(?P<type>[\w-]+)/$', views.details, name='details'),
]
