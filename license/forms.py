from django import forms
from .models import License

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['category', 'title', 'sub_title','description', 'cost', 'unit', 'terms', 'license_type']