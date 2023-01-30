from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from pagedown.widgets import AdminPagedownWidget

from .models import Fair


class PageDownAdmin(TranslationAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


@admin.register(Fair)
class FairAdmin(PageDownAdmin):
    list_display = ('name', 'location', 'start', 'end', 'archive', 'public', 'created')
    list_filter = ['created']
    search_fields = ['name']
    fieldsets = [
        (_('Allgemein'), {'fields': ['name', 'website', 'location', ('hall', 'stand'),
         ('start', 'end'), 'description', ('image', 'attachment'), ('archive', 'public')]}),
        (_('Erweitert'), {'fields': ['created'], 'classes': ['collapse']}),
    ]
