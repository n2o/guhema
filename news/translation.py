from modeltranslation.translator import TranslationOptions, register

from .models import Entry


@register(Entry)
class EntryTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
