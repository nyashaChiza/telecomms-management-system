from django.shortcuts import render
from license.models import *#License, LicenseApplication, EquipmentApprovalApplication, 
from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_logout_view(request):
    logout(request)
    return redirect('home')


def index(request, **kwargs):
    licenses = License.objects.all()
    equipment_approval_applications = EquipmentApprovalApplication.objects.all()
    private_network_applications = PrivateMobileNetworkLicenseApplication.objects.all()
    frequency_allocation_applications = FrequencySpectrumAllocationLicenseApplication.objects.all()
    coverage_applications = CoverageLicenseApplication.objects.all()
    context = {'licenses':licenses.count(), 'applications':sum([equipment_approval_applications.count(), private_network_applications.count(), frequency_allocation_applications.count(), coverage_applications.count()])} 
    
    return render(request, 'admin/index.html', context = context)

def license_index(request, **kwargs):
    licenses = License.objects.all()
    equipment_approval_applications = EquipmentApprovalApplication.objects.all()
    private_network_applications = PrivateMobileNetworkLicenseApplication.objects.all()
    frequency_allocation_applications = FrequencySpectrumAllocationLicenseApplication.objects.all()
    coverage_applications = CoverageLicenseApplication.objects.all()
    context = {'obj':licenses,'licenses':licenses.count(), 'applications':sum([equipment_approval_applications.count(), private_network_applications.count(), frequency_allocation_applications.count(), coverage_applications.count()])} 
    
    return render(request, 'admin/license.html', context = context)

