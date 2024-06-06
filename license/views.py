from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import License
from django.db import models
from .forms import LicenseForm, LicenseSearchForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.forms import ModelForm, HiddenInput
from .forms import (
    EquipmentApprovalApplicationForm,
    PrivateMobileNetworkLicenseApplicationForm,
    FrequencySpectrumAllocationLicenseApplicationForm,
    CoverageLicenseApplicationForm,
)
from license.models import (
    EquipmentApprovalApplication,
    PrivateMobileNetworkLicenseApplication,
    FrequencySpectrumAllocationLicenseApplication,
    CoverageLicenseApplication,
)
from django.contrib.auth.decorators import login_required
 
def license_list(request):
    licenses = License.objects.all()
    return render(request, 'license_list.html', {'licenses': licenses})

def license_detail(request, pk):
    license = get_object_or_404(License, pk=pk)
    return render(request, 'web/details.html', {'license': license})

def license_create(request):
    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            license = form.save()
            return redirect('admin_license_index')
    else:
        form = LicenseForm()
    licenses = License.objects.all()
    equipment_approval_applications = EquipmentApprovalApplication.objects.all()
    private_network_applications = PrivateMobileNetworkLicenseApplication.objects.all()
    frequency_allocation_applications = FrequencySpectrumAllocationLicenseApplication.objects.all()
    coverage_applications = CoverageLicenseApplication.objects.all()
    context = {'form': form, 'obj':licenses,'licenses':licenses.count(), 'applications':sum([equipment_approval_applications.count(), private_network_applications.count(), frequency_allocation_applications.count(), coverage_applications.count()])} 
    
   

    return render(request, 'admin/licenses/create.html', context)

def license_update(request, pk):
    license = get_object_or_404(License, pk=pk)
    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            license = form.save()
            return redirect('license_detail', pk=license.pk)
    else:
        form = LicenseForm(instance=license)
    return render(request, 'license_update.html', {'form': form})

def license_delete(request, pk):
    license = get_object_or_404(License, pk=pk)
    if request.method == 'POST':
        license.delete()
        return redirect('license_list')
    return render(request, 'license_delete.html', {'license': license})

def search_licenses(request):
    form = LicenseSearchForm(request.GET)
    licenses = License.objects.all()

    if form.is_valid():
        location = form.cleaned_data.get('location')
        keyword = form.cleaned_data.get('keyword')

        if location:
            licenses = licenses.filter(location__icontains=location)
        if keyword:
            licenses = licenses.filter(
                models.Q(category__icontains=keyword) |
                models.Q(title__icontains=keyword) |
                models.Q(sub_title__icontains=keyword) |
                models.Q(description__icontains=keyword) |
                models.Q(tag__icontains=keyword)
            )

    return render(request, 'web/search.html', {'form': form, 'licenses': licenses})




class LicenseFormMixin(ModelForm):
    class Meta:
        model = License
        fields = '__all__'

@login_required
def get_application_form_view(request, pk):
    application_type = request.GET.get('type')
    license = License.objects.filter(pk=pk).first()

    if not license:
        return HttpResponseNotFound("License not found")

    if application_type == 'equipment_approval':
        form_class = EquipmentApprovalApplicationForm
    elif application_type == 'private_mobile_network':
        form_class = PrivateMobileNetworkLicenseApplicationForm
    elif application_type == 'frequency_spectrum_allocation':
        form_class = FrequencySpectrumAllocationLicenseApplicationForm
    elif application_type == 'coverage_licensing':
        form_class = CoverageLicenseApplicationForm
    else:
        return HttpResponseNotFound("Application type not found")

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # Merge the license data into the form instance
            form_instance = form.save(commit=False)
            form_instance.license = license
            form_instance.save()
            return redirect('products')  # Redirect to a success page
    else:
        # Create form instance and merge the license data
        form = form_class(initial={'license': license.pk})
        form.fields['license'].widget = HiddenInput()

    return render(request, 'web/application.html', {'form': form, 'license':license, 'application_type': application_type})
