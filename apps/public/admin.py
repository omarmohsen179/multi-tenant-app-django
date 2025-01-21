from django.contrib import admin
from .models import SharedResource

@admin.register(SharedResource)
class SharedResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
