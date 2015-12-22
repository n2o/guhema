# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^maschinensaegeblatt/$', views.sawblades, {'title': "Maschinensägeblätter"}, name='sawblades'),
    url(r'^maschinensaegeblatt/(?P<clamping>[\w-]+)/(?P<slug>[\w-]+)/$', views.sawblade, name='sawblade'),
]