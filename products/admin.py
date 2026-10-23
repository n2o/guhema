from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from core.admin import PageDownAdmin

from .models import (BandSawBlade, BandSawBladeIndicator, CircularSawBlade,
                     CircularSawBladeIndicator, Clamping, HackSawBlade,
                     HoleSaw, HoleSawDiameter, Indicator, JigSawBlade,
                     ProductGroup, SableSawBlade, SawBlade)


class ProductAdmin(PageDownAdmin):
    @admin.display(boolean=True, description=_("Bild"))
    def has_img_set(self, obj):
        return bool(obj.image)


@admin.register(SawBlade)
class SawBladeAdmin(ProductAdmin):
    list_display = ('type', 'group', 'quality', 'has_img_set')
    search_fields = ['type', 'quality', 'description']


@admin.register(SableSawBlade)
class SableSawBladeAdmin(ProductAdmin):
    list_display = ('type', 'group', 'quality', 'toothing', 'cutting_metal', 'cutting_wood', 'cutting_minerals', 'has_img_set')
    search_fields = ['type', 'quality', 'description']
    save_as = True


@admin.register(HackSawBlade)
class HackSawBladeAdmin(ProductAdmin):
    list_display = ('type', 'group', 'quality', 'toothing', 'accessory', 'cutting_metal', 'cutting_wood', 'cutting_minerals', 'has_img_set')
    search_fields = ['type', 'quality', 'description']
    fieldsets = [
        (_('Allgemein'), {'fields': ['quality', 'type', 'name', 'subcategory', 'description', 'group']}),
        (_('Beschreibung'), {'fields': ['image', 'indicators', 'toothing', ('cutting_metal', 'cutting_wood', 'cutting_minerals'), 'accessory']}),
    ]
    save_as = True


@admin.register(Indicator)
class IndicatorAdmin(PageDownAdmin):
    fieldsets = [
        (_('Allgemein'), {'fields': ['value']}),
        (_('Abmessungen'), {'fields': ['width', 'strength', 'length', 'diameter']}),
        (_('ZpZ'), {'fields': [('C', 'E', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'T', 'U', 'V', 'W', 'UE')]}),
    ]


@admin.register(HoleSaw)
class HoleSawAdmin(ProductAdmin):
    list_display = ('ordernr', 'category', 'has_img_set')
    search_fields = ['ordernr']


@admin.register(ProductGroup)
class ProductGroupAdmin(PageDownAdmin):
    list_display = ('name', 'public')
    fieldsets = [
        (_('Allgemein'), {'fields': ['name', 'description', 'image', 'public']}),
    ]


@admin.register(BandSawBlade)
class BandSawBladeAdmin(ProductAdmin):
    list_display = ('type', 'type2', 'group', 'quality', 'has_img_set')
    search_fields = ['type', 'type2', 'quality', 'description']
    fieldsets = [
        (_('Allgemein'), {'fields': ['quality', 'name', 'heading', 'description', 'group']}),
        (_('Ausführungen'), {'fields': [('type', 'type_description'), ('type2', 'type2_description'), ('image', 'image2'), 'bandsaw_indicators', 'cols']}),
    ]


@admin.register(JigSawBlade)
class JigSawBladeAdmin(ProductAdmin):
    list_display = ('type', 'subcategory', 'has_img_set')
    search_fields = ['type', 'subcategory']
    fieldsets = [
        (_('Allgemein'), {'fields': ['quality', 'subcategory', 'description', 'group']}),
        (_('Ausführungen'), {'fields': ['type', 'image', 'tooth_separation', 'length', ('cutting_metal', 'cutting_wood')]}),
    ]


@admin.register(CircularSawBlade)
class CircularSawBladeAdmin(ProductAdmin):
    list_display = ('type', 'quality', 'has_img_set')
    search_fields = ['type']
    fieldsets = [
        (_('Allgemein'), {'fields': ['quality', 'type', 'name', 'description', 'group']}),
        (_('Kennziffer') + '1', {'fields': ['circular_indicators']}),
    ]


# Define a new FlatPageAdmin
class MyFlatPageAdmin(PageDownAdmin):
    fieldsets = (
        (_('Allgemein'), {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


admin.site.register(CircularSawBladeIndicator)
admin.site.register(BandSawBladeIndicator)
admin.site.register(Clamping, TranslationAdmin)
admin.site.register(HoleSawDiameter)

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)
