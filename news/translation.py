from modeltranslation.translator import register, TranslationOptions
from .models import Entry


@register(Entry)
class EntryTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
