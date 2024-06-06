from web.views import *
from django.urls import path

urlpatterns = [
  
    path('', index, name="home"),
    path('products/', ProductListView.as_view(), name="products"),
    path('contact/', contact, name="contact"),
    path('admins/login/', admin_login_view, name='admins_login'),
    path('user/login/', user_login_view, name='user_login'),
    path('signup/', signup_view, name="signup"),
]
