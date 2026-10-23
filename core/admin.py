from django.db import models
from modeltranslation.admin import TranslationAdmin
from pagedown.widgets import AdminPagedownWidget


class PageDownAdmin(TranslationAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }
