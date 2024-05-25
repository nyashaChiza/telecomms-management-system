from django.shortcuts import render
from license.models import License
from django.views.generic import ListView

def index(request, **kwargs):
    return render(request, 'web/index.html')

class ProductListView(ListView):
    model = License
    template_name = 'web/products.html'
    context_object_name = 'licenses'
    queryset = License.objects.filter(status='active').all()

def contact(request, **kwargs):
    return render(request, 'web/contact.html')