from django import forms
from .models import License

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['category', 'title', 'sub_title','description', 'cost', 'unit', 'terms', 'license_type']

class LicenseSearchForm(forms.Form):
    location = forms.CharField(max_length=250, required=False)
    keyword = forms.CharField(max_length=100, required=False)