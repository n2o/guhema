from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models

from .models import Indicator, SawBlade, Clamping, ProductGroup


class PageDownAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


@admin.register(SawBlade)
class SawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'name', 'description', 'clamping')
    search_fields = ['type', 'name', 'description']


@admin.register(Indicator)
class IndicatorAdmin(PageDownAdmin):
    fieldsets = [
        ('Allgemein', {'fields': ['value']}),
        ('Abmessungen', {'fields': ['width', 'strength', 'length', 'diameter']}),
        ('ZpZ', {'fields': [('C', 'E', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'T', 'U', 'V', 'W', 'UE')]}),
    ]


@admin.register(ProductGroup)
class ProductGroupAdmin(PageDownAdmin):
    list_display = ('name', 'public')


admin.site.register(Clamping)
