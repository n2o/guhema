from django.contrib import admin
from .models import Indicator, SawBlade, Clamping, ProductGroup


@admin.register(SawBlade)
class SawBladeAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'description', 'clamping')
    search_fields = ['type', 'name', 'description']


@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Allgemein', {'fields': ['value']}),
        ('Abmessungen', {'fields': ['width', 'strength', 'length', 'diameter']}),
        ('ZpZ', {'fields': [('C', 'E', 'G', 'H', 'I', 'J', 'L', 'N', 'O', 'T', 'U', 'V', 'W', 'UE')]}),
    ]


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'public')


admin.site.register(Clamping)
