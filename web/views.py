from django.shortcuts import render


def index(request, **kwargs):
    return render(request, 'web/index.html')

def products(request, **kwargs):
    return render(request, 'web/products.html')


def contact(request, **kwargs):
    return render(request, 'web/contact.html')