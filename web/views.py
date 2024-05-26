from django.shortcuts import render
from license.models import License
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AdminLoginForm

def index(request, **kwargs):
    return render(request, 'web/index.html')

class ProductListView(ListView):
    model = License
    template_name = 'web/products.html'
    context_object_name = 'licenses'
    queryset = License.objects.filter(status='Active').all()

def contact(request, **kwargs):
    return render(request, 'web/contact.html')



def admin_login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:  # Only allow staff users to log in
                    login(request, user)
                    return redirect('admin_index')  # Redirect to your admin dashboard
                else:
                    messages.error(request, 'You do not have permission to access this area.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AdminLoginForm()

    return render(request, 'web/signin.html', {'form': form})
