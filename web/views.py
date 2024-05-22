from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
def index(request, **kwargs):
    return render(request, 'web/index.html')