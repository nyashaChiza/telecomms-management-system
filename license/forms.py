from django import forms
from .models import (
    License,
    LicenseApplication,
    EquipmentApprovalApplication,
    PrivateMobileNetworkLicenseApplication,
    FrequencySpectrumAllocationLicenseApplication,
    CoverageLicenseApplication,
)

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['category', 'title', 'sub_title','location', 'description', 'cost', 'unit', 'terms', 'license_type']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'terms': forms.Textarea(attrs={'class': 'form-control'}),
            'license_type': forms.Select(attrs={'class': 'form-control'}),
        }

class LicenseSearchForm(forms.Form):
    location = forms.CharField(max_length=250, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    keyword = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = LicenseApplication
        fields = '__all__'
        exclude = ['status']
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'form-control'}) for field in LicenseApplication._meta.fields if field.name != 'status'
        }
        widgets.update({
            field.name: forms.Textarea(attrs={'class': 'form-control'}) for field in LicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.TextInput)
        })
        widgets.update({
            field.name: forms.EmailInput(attrs={'class': 'form-control'}) for field in LicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.EmailInput)
        })

class EquipmentApprovalApplicationForm(forms.ModelForm):
    class Meta:
        model = EquipmentApprovalApplication
        fields = '__all__'
        exclude = ['status']
        # widgets = {
        #     field.name: forms.TextInput(attrs={'class': 'form-control'}) for field in EquipmentApprovalApplication._meta.fields if field.name != 'status'
        # }
        # widgets.update({
        #     field.name: forms.Textarea(attrs={'class': 'form-control'}) for field in EquipmentApprovalApplication._meta.fields if field.name != 'status' and isinstance(field, forms.TextInput)
        # })
        # widgets.update({
        #     field.name: forms.EmailInput(attrs={'class': 'form-control'}) for field in EquipmentApprovalApplication._meta.fields if field.name != 'status' and isinstance(field, forms.EmailInput)
        # })

class PrivateMobileNetworkLicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = PrivateMobileNetworkLicenseApplication
        fields = '__all__'
        exclude = ['status']
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'form-control'}) for field in PrivateMobileNetworkLicenseApplication._meta.fields if field.name != 'status'
        }
        widgets.update({
            field.name: forms.Textarea(attrs={'class': 'form-control'}) for field in PrivateMobileNetworkLicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.TextInput)
        })
        widgets.update({
            field.name: forms.EmailInput(attrs={'class': 'form-control'}) for field in PrivateMobileNetworkLicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.EmailInput)
        })

class FrequencySpectrumAllocationLicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = FrequencySpectrumAllocationLicenseApplication
        fields = '__all__'
        exclude = ['status']
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'form-control'}) for field in FrequencySpectrumAllocationLicenseApplication._meta.fields if field.name != 'status'
        }
        widgets.update({
            field.name: forms.Textarea(attrs={'class': 'form-control'}) for field in FrequencySpectrumAllocationLicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.TextInput)
        })
        widgets.update({
            field.name: forms.EmailInput(attrs={'class': 'form-control'}) for field in FrequencySpectrumAllocationLicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.EmailInput)
        })

class CoverageLicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = CoverageLicenseApplication
        fields = '__all__'
        widgets = {
            field.name: forms.TextInput(attrs={'class': 'form-control'}) for field in CoverageLicenseApplication._meta.fields if field.name != 'status'
        }
        widgets.update({
            field.name: forms.Textarea(attrs={'class': 'form-control'}) for field in CoverageLicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.TextInput)
        })
        widgets.update({
            field.name: forms.EmailInput(attrs={'class': 'form-control'}) for field in CoverageLicenseApplication._meta.fields if field.name != 'status' and isinstance(field, forms.EmailInput)
        })
