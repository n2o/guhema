from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.admin import PageDownAdmin

from .models import Category, Entry


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
        if obj.author is None:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
