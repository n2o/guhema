from django.contrib import admin
from .models import Indicator, SawBlade


class IndicatorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Allgemein', {'fields': ['value', 'hss']}),
        ('Abmessungen', {'fields': ['width', 'strength', 'length', 'diameter']})
    ]


admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(SawBlade)
