from django.contrib import admin

from .models import Tooth, Indicator, SawBlade

admin.site.register(Tooth)
admin.site.register(Indicator)
admin.site.register(SawBlade)