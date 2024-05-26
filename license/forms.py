from django import forms
from .models import License
from .models import LicenseApplication, EquipmentApprovalApplication, PrivateMobileNetworkLicenseApplication, FrequencySpectrumAllocationLicenseApplication, CoverageLicenseApplication

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['category', 'title', 'sub_title','description', 'cost', 'unit', 'terms', 'license_type']

class LicenseSearchForm(forms.Form):
    location = forms.CharField(max_length=250, required=False)
    keyword = forms.CharField(max_length=100, required=False)
    


class LicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = LicenseApplication
        fields = '__all__'
        exclude = ['status']
        
class EquipmentApprovalApplicationForm(forms.ModelForm):
    class Meta:
        model = EquipmentApprovalApplication
        fields = '__all__'
        exclude = ['status']

class PrivateMobileNetworkLicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = PrivateMobileNetworkLicenseApplication
        fields = '__all__'
        exclude = ['status']


class FrequencySpectrumAllocationLicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = FrequencySpectrumAllocationLicenseApplication
        fields = '__all__'
        exclude = ['status']


class CoverageLicenseApplicationForm(forms.ModelForm):
    class Meta:
        model = CoverageLicenseApplication
        fields = '__all__'
        
