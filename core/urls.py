from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpageviews

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # 3rd party

    # Own Apps
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^produkte/', include('products.urls', namespace='products')),
    url(r'^messen/', include('fairs.urls', namespace='fairs')),
    url(r'^kontakt/', include('contact.urls', namespace='contact')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    url(r'^unternehmen/$', views.company, name='company'),
    url(r'^impressum/$', flatpageviews.flatpage, {'url': '/impressum/'}, name='impressum'),

    url(r'^(?P<url>.*/)$', flatpageviews.flatpage, name='page'),
]
