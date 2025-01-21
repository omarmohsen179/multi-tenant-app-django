from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Tenant, Domain

@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'paid_until', 'on_trial', 'created_on']
    search_fields = ['name']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['domain', 'tenant', 'is_primary']
    search_fields = ['domain']
