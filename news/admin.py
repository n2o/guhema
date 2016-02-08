from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.db import models
from pagedown.widgets import AdminPagedownWidget
from django.utils.translation import ugettext_lazy as _


from .models import Category, Entry


class PageDownAdmin(TranslationAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }


@admin.register(Entry)
class NewsAdmin(PageDownAdmin):
    list_display = ('title', 'category', 'archive', 'public', 'created')
    list_filter = ['created']
    search_fields = ['title']
    fieldsets = [
        (None,        {'fields': ['title', 'category', 'image', 'attachment', ('archive', 'public'), 'content']}),
        (_('Erweitert'), {'fields': ['created', 'author'], 'classes': ['collapse']}),
    ]

    def save_model(self, request, obj, form, change):
        # Automatic set author if None is set
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Category)
