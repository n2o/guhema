from django.contrib.flatpages.models import FlatPage
from modeltranslation.translator import (TranslationOptions, register,
                                         translator)

from .models import (BandSawBlade, CircularSawBlade, HackSawBlade, HoleSaw,
                     Indicator, JigSawBlade, ProductGroup, SableSawBlade,
                     SawBlade)


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(SawBlade)
class SawBladeTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(SableSawBlade)
class SableSawBladeTranslationOptions(TranslationOptions):
    fields = ('cutting_minerals', 'toothing')


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


translator.register(HackSawBlade, SawBladeTranslationOptions)
translator.register(CircularSawBlade, SawBladeTranslationOptions)
translator.register(Indicator, NoTranslationOptions)
translator.register(FlatPage, NoTranslationOptions)
