from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib.flatpages import views as flatpageviews


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/', include('login.urls', namespace='login')),

    # 3rd party

    # Own Apps
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^produkte/', include('products.urls', namespace='products')),
    url(r'^kontakt/', include('contact.urls', namespace='contact')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    url(r'^unternehmen/$', flatpageviews.flatpage, {'url': '/unternehmen/'}, name='company'),
    url(r'^impressum/$', flatpageviews.flatpage, {'url': '/impressum/'}, name='impressum'),

    url(r'^(?P<url>.*/)$', flatpageviews.flatpage, name='page'),
]