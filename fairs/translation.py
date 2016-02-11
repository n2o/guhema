from modeltranslation.translator import TranslationOptions, register

from .models import Fair


@register(Fair)
class FairTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
