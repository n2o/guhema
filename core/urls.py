from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),

    # Own Apps
    url(r'^news/', include('news.urls', namespace='news')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
