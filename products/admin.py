from django.contrib import admin
from .models import Indicator, SawBlade


class IndicatorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Allgemein', {'fields': ['value', 'hss']}),
        ('Abmessungen', {'fields': ['width', 'strength', 'length', 'diameter']}),
        ('ZpZ', {'fields': [('C', 'E', 'G', 'H', 'I', 'J', 'L', 'N', 'O', 'T', 'U', 'V', 'W', 'UE')]}),
    ]


admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(SawBlade)
