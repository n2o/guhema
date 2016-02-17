from django.contrib.flatpages.models import FlatPage
from modeltranslation.translator import (TranslationOptions, register,
                                         translator)

from .models import (BandSawBlade, CircularSawBlade, HackSawBlade, HoleSaw,
                     Indicator, JigSawBlade, ProductGroup, SableSawBlade,
                     SawBlade, Clamping)


@register(Clamping)
class ClampingTranslationOptions(TranslationOptions):
    fields = ('image',)


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(SawBlade)
class SawBladeTranslationOptions(TranslationOptions):
    fields = ('description', 'name')


@register(SableSawBlade)
class SableSawBladeTranslationOptions(TranslationOptions):
    fields = ('cutting_minerals', 'toothing')


@register(HackSawBlade)
class HackSawBladeTranslationOptions(TranslationOptions):
    fields = ('subcategory',)


@register(HoleSaw)
class HoleSawTranslationOptions(TranslationOptions):
    fields = ('description', 'category', 'mounting')


@register(BandSawBlade)
class BandSawBladeTranslationOptions(TranslationOptions):
    fields = ('type_description', 'type2_description', 'heading')


@register(JigSawBlade)
class JigSawBladeTranslationOptions(TranslationOptions):
    fields = ('subcategory',)


class NoTranslationOptions(TranslationOptions):
    pass


translator.register(CircularSawBlade, SawBladeTranslationOptions)
translator.register(Indicator, NoTranslationOptions)
translator.register(FlatPage, NoTranslationOptions)
