from web.views import *
from django.urls import path

urlpatterns = [
    path('', index, name="home"),
    path('products/', ProductListView.as_view(), name="products"),
    path('contact/', contact, name="contact"),
      path('admins/login/', admin_login_view, name='admins_login'),
]
