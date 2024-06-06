from portal.views import *
from django.urls import path
from license.views import *

urlpatterns = [
    path('', index, name="admins_index"),
    path('logout/', admin_logout_view, name="signout"),
    path('licenses/', license_index, name="admin_license_index"),
    path('equipment-approval/create/', EquipmentApprovalApplicationCreateView.as_view(), name='equipment-approval-create'),
    path('private-mobile-network/create/', PrivateMobileNetworkLicenseApplicationCreateView.as_view(), name='private-mobile-network-create'),
    path('frequency-spectrum-allocation/create/', FrequencySpectrumAllocationLicenseApplicationCreateView.as_view(), name='frequency-spectrum-allocation-create'),
    path('coverage-license/create/', CoverageLicenseApplicationCreateView.as_view(), name='coverage-license-create'),
]
