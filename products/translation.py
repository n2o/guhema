from modeltranslation.translator import register, TranslationOptions
from .models import ProductGroup, SawBlade, HoleSaw, BandSawBlade, JigSawBlade


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
