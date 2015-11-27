from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^maschinensaegeblatt/$', views.sawblades, name='sawblades'),
    url(r'^maschinensaegeblatt/(?P<slug>[\w-]+)/$', views.sawblade, name='sawblade'),
]