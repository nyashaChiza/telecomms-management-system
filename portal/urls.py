from portal.views import *
from django.urls import path

urlpatterns = [
    path('', index, name="admin_index"),
    path('logout/', admin_logout_view, name="signout"),
    path('licenses/', license_index, name="admin_license_index"),
    

]
