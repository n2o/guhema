from modeltranslation.translator import register, TranslationOptions
from .models import Fair


@register(Fair)
class FairTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
