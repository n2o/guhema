# -*- coding: utf-8 -*-
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^lochsagen/empfehlung$', views.holesawAdvice, name='holesaw_advice'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.list, name='list'),
    re_path(r'^(?P<slug>[\w-]+)/details$', views.product_details, name='product_details'),
    re_path(r'^(?P<slug>[\w-]+)/empfehlungen$', views.product_advices, name='advices'),
    re_path(r'^(?P<slug>[\w-]+)/(?P<id>[0-9]+)/$', views.details_by_id, name='details_by_id'),
    re_path(r'^(?P<slug>[\w-]+)/(?P<type>[\w-]+)/$', views.details, name='details'),
]
