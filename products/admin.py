from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models

from .models import Indicator, SawBlade, Clamping, ProductGroup, SableSawBlade, HackSawBlade


class PageDownAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


@admin.register(SawBlade)
class SawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'quality')
    search_fields = ['type', 'quality', 'description']


@admin.register(SableSawBlade)
class SableSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'quality', 'toothing', 'cutting_metal', 'cutting_wood', 'cutting_minerals')
    search_fields = ['type', 'quality', 'description']
    save_as = True


@admin.register(HackSawBlade)
class HackSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'quality', 'toothing', 'accessory', 'cutting_metal', 'cutting_wood', 'cutting_minerals')
    search_fields = ['type', 'quality', 'description']
    save_as = True


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
