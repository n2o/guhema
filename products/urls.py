# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lochsagen/empfehlung$', views.holesawAdvice, name='holesaw_advice'),
    url(r'^(?P<slug>[\w-]+)/$', views.list, name='list'),
    url(r'^(?P<slug>[\w-]+)/details$', views.productDetails, name='product_details'),
    url(r'^(?P<slug>[\w-]+)/details/empfehlungen$', views.productAdvices, name='product_advices'),
    url(r'^(?P<slug>[\w-]+)/(?P<id>[0-9]+)/$', views.detailsById, name='details_by_id'),
    url(r'^(?P<slug>[\w-]+)/(?P<type>[\w-]+)/$', views.details, name='details'),
]
