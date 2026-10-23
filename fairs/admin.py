from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import PageDownAdmin

from .models import Fair


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
