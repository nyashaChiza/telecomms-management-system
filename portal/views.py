from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_logout_view(request):
    logout(request)
    return redirect('home')

def index(request, **kwargs):
    return render(request, 'admin/index.html')

