from web.views import *
from django.urls import path

urlpatterns = [
    path('', index, name="home"),
]
