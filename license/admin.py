from django.contrib import admin
from .models import License

from django.contrib import admin
from .models import (
    License, LicenseApplication, EquipmentApprovalApplication,
    PrivateMobileNetworkLicenseApplication, FrequencySpectrumAllocationLicenseApplication,
    CoverageLicenseApplication
)

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'cost', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description', 'tag')
    fieldsets = (
        (None, {
            'fields': ('title','sub_title', 'category', 'description', 'tag', 'application_type')
        }),
        ('Pricing', {
            'fields': ('cost', 'unit')
        }),
        ('Status', {
            'fields': ('status', 'terms', 'license_type', 'location')
        }),
    )
    


class EquipmentApprovalApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'license', 'status']
    search_fields = ['title', 'license__title']
    list_filter = ['status']
    list_per_page = 20
    date_hierarchy = 'application_date'

class PrivateMobileNetworkLicenseApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'license', 'status']
    search_fields = ['title', 'license__title']
    list_filter = ['status']
    list_per_page = 20
    date_hierarchy = 'application_date'

class FrequencySpectrumAllocationLicenseApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'license', 'status']
    search_fields = ['title', 'license__title']
    list_filter = ['status']
    list_per_page = 20
    date_hierarchy = 'application_date'

class CoverageLicenseApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'license', 'status']
    search_fields = ['title', 'license__title']
    list_filter = ['status']
    list_per_page = 20
    date_hierarchy = 'application_date'

admin.site.register(EquipmentApprovalApplication, EquipmentApprovalApplicationAdmin)
admin.site.register(PrivateMobileNetworkLicenseApplication, PrivateMobileNetworkLicenseApplicationAdmin)
admin.site.register(FrequencySpectrumAllocationLicenseApplication, FrequencySpectrumAllocationLicenseApplicationAdmin)
admin.site.register(CoverageLicenseApplication, CoverageLicenseApplicationAdmin)
