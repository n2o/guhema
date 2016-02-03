from modeltranslation.translator import register, TranslationOptions, translator
from .models import ProductGroup, SawBlade, HoleSaw, BandSawBlade, JigSawBlade, SableSawBlade, HackSawBlade, Indicator, \
    CircularSawBlade
from django.contrib.flatpages.models import FlatPage


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(SawBlade)
class SawBladeTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(HoleSaw)
class HoleSawTranslationOptions(TranslationOptions):
    fields = ('description', 'category',)


@register(BandSawBlade)
class BandSawBladeTranslationOptions(TranslationOptions):
    fields = ('type_description', 'type2_description',)


@register(JigSawBlade)
class JigSawBladeTranslationOptions(TranslationOptions):
    fields = ('subcategory',)


class NoTranslationOptions(TranslationOptions):
    pass


translator.register(SableSawBlade, SawBladeTranslationOptions)
translator.register(HackSawBlade, SawBladeTranslationOptions)
translator.register(CircularSawBlade, SawBladeTranslationOptions)
translator.register(Indicator, NoTranslationOptions)
translator.register(FlatPage, NoTranslationOptions)