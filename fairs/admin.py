from django.contrib import admin
from .models import Fair


@admin.register(Fair)
class FairAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start', 'end', 'archive', 'public', 'created')
    list_filter = ['created']
    search_fields = ['name']
    fieldsets = [
        ('Allgemein', {'fields': ['name', 'location', ('hall', 'stand'), 'start', 'end', ('archive', 'public'), 'description', ('image', 'attachment')]}),
        ('Erweitert', {'fields': ['created'], 'classes': ['collapse']}),
    ]