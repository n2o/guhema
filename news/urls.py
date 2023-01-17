from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.overview, {'category': 'Allgemein'}, name='overview'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
]
