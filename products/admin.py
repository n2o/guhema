from django.contrib import admin
from django.utils.safestring import mark_safe
from pagedown.widgets import AdminPagedownWidget
from django.db import models

from .models import Indicator, SawBlade, Clamping, ProductGroup, SableSawBlade, HackSawBlade, HoleSaw, HoleSawDiameter, BandSawBlade, BandSawBladeIndicator, JigSawBlade, CircularSawBlade, CircularSawBladeIndicator


class PageDownAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }

    def has_img_set(self, obj):
        if obj.image:
            return mark_safe("<img src='/static/admin/img/icon-yes.svg' alt='True'>")
        else:
            return mark_safe("<img src='/static/admin/img/icon-no.svg' alt='False'>")


@admin.register(SawBlade)
class SawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'quality', 'has_img_set')
    search_fields = ['type', 'quality', 'description']


@admin.register(SableSawBlade)
class SableSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'quality', 'toothing', 'cutting_metal', 'cutting_wood', 'cutting_minerals', 'has_img_set')
    search_fields = ['type', 'quality', 'description']
    save_as = True


@admin.register(HackSawBlade)
class HackSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'group', 'quality', 'toothing', 'accessory', 'cutting_metal', 'cutting_wood', 'cutting_minerals', 'has_img_set')
    search_fields = ['type', 'quality', 'description']
    save_as = True


@admin.register(Indicator)
class IndicatorAdmin(PageDownAdmin):
    fieldsets = [
        ('Allgemein', {'fields': ['value']}),
        ('Abmessungen', {'fields': ['width', 'strength', 'length', 'diameter']}),
        ('ZpZ', {'fields': [('C', 'E', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'T', 'U', 'V', 'W', 'UE')]}),
    ]


@admin.register(HoleSaw)
class HoleSawAdmin(PageDownAdmin):
    list_display = ('ordernr', 'category', 'has_img_set')
    search_fields = ['ordernr']


@admin.register(ProductGroup)
class ProductGroupAdmin(PageDownAdmin):
    list_display = ('name', 'public')


@admin.register(BandSawBlade)
class BandSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'type2', 'group', 'quality', 'has_img_set')
    search_fields = ['type', 'type2', 'quality', 'description']
    fieldsets = [
        ('Allgemein', {'fields': ['quality', 'name', 'heading', 'description', 'group']}),
        ('Ausführungen', {'fields': [('type', 'type_description'), ('type2', 'type2_description'), ('image', 'image2'), 'bandsaw_indicators', 'cols']}),
    ]


@admin.register(JigSawBlade)
class JigSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'subcategory', 'has_img_set')
    search_fields = ['type', 'subcategory']
    fieldsets = [
        ('Allgemein', {'fields': ['quality', 'subcategory', 'description', 'group']}),
        ('Ausführungen', {'fields': ['type', 'image', 'tooth_separation', 'length', ('cutting_metal', 'cutting_wood')]}),
    ]


@admin.register(CircularSawBlade)
class CircularSawBladeAdmin(PageDownAdmin):
    list_display = ('type', 'quality', 'has_img_set')
    search_fields = ['type']
    fieldsets = [
        ('Allgemein', {'fields': ['quality', 'type', 'name', 'description', 'group']}),
        ('Kennziffer 1', {'fields': ['circular_indicators']}),
    ]


admin.site.register(CircularSawBladeIndicator)
admin.site.register(BandSawBladeIndicator)
admin.site.register(Clamping)
admin.site.register(HoleSawDiameter)
