from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views as flatpageviews
from django.urls import re_path

from . import views

urlpatterns = [
                  re_path(r'^$', views.index, name='index'),
                  re_path(r'^pages/', include('django.contrib.flatpages.urls')),
                  re_path(r'^admin/', admin.site.urls),
                  re_path(r'^i18n/', include('django.conf.urls.i18n')),

                  # 3rd party

                  # Own Apps
                  re_path(r'^news/', include(('news.urls', 'news'), namespace='news')),
                  re_path(r'^kataloge/', include(('downloads.urls', 'downloads'), namespace='downloads')),
                  re_path(r'^produkte/', include(('products.urls', 'products'), namespace='products')),
                  re_path(r'^messen/', include(('fairs.urls', 'fairs'), namespace='fairs')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Named Staticpages
urlpatterns += [
    re_path(r'^unternehmen/$', views.company, name='company'),
    re_path(r'^impressum/$', flatpageviews.flatpage, {'url': '/impressum/'}, name='impressum'),
    re_path(r'^datenschutz/$', flatpageviews.flatpage, {'url': '/datenschutz/'}, name='datenschutz'),

    re_path(r'^(?P<url>.*/)$', flatpageviews.flatpage, name='page'),
]
