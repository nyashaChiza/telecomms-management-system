from portal.views import *
from django.urls import path

urlpatterns = [
    path('', index, name="admin_index"),
    path('logout/', admin_logout_view, name="signout"),
    

]
