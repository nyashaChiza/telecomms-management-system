from django.shortcuts import render, get_object_or_404, redirect
from .models import License
from .forms import LicenseForm

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
            return redirect('license_detail', pk=license.pk)
    else:
        form = LicenseForm()
    return render(request, 'license_create.html', {'form': form})

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