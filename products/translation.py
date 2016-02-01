from modeltranslation.translator import register, TranslationOptions
from .models import ProductGroup


@register(ProductGroup)
class ProductGroupTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)