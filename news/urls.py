from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.overview, {'category': 'Allgemein'}, name='overview'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
]
