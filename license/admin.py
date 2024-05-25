from django.contrib import admin
from .models import License

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'cost', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'description')
        }),
        ('Pricing', {
            'fields': ('cost', 'unit')
        }),
        ('Status', {
            'fields': ('status', 'terms', 'license_type')
        }),
    )