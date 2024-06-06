from django.shortcuts import render
from license.models import *#License, LicenseApplication, EquipmentApprovalApplication, 
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from license.models import (
    EquipmentApprovalApplication,
    PrivateMobileNetworkLicenseApplication,
    FrequencySpectrumAllocationLicenseApplication,
    CoverageLicenseApplication,
)
from license.forms import (
    EquipmentApprovalApplicationForm,
    PrivateMobileNetworkLicenseApplicationForm,
    FrequencySpectrumAllocationLicenseApplicationForm,
    CoverageLicenseApplicationForm,
)

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



class EquipmentApprovalApplicationCreateView(CreateView):
    model = EquipmentApprovalApplication
    form_class = EquipmentApprovalApplicationForm
    template_name = 'admin/licenses/equipment_approval_form.html'
    success_url = reverse_lazy('equipment-approval-list')

class PrivateMobileNetworkLicenseApplicationCreateView(CreateView):
    model = PrivateMobileNetworkLicenseApplication
    form_class = PrivateMobileNetworkLicenseApplicationForm
    template_name = 'licenses/private_mobile_network_form.html'
    success_url = reverse_lazy('private-mobile-network-list')

class FrequencySpectrumAllocationLicenseApplicationCreateView(CreateView):
    model = FrequencySpectrumAllocationLicenseApplication
    form_class = FrequencySpectrumAllocationLicenseApplicationForm
    template_name = 'licenses/frequency_spectrum_allocation_form.html'
    success_url = reverse_lazy('frequency-spectrum-allocation-list')

class CoverageLicenseApplicationCreateView(CreateView):
    model = CoverageLicenseApplication
    form_class = CoverageLicenseApplicationForm
    template_name = 'licenses/coverage_license_form.html'
    success_url = reverse_lazy('coverage-license-list')
