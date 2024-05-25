from django.urls import path
from . import views

urlpatterns = [
    path('licenses/', views.license_list, name='license_list'),
    path('licenses/create/', views.license_create, name='license_create'),
    path('licenses/<int:pk>/', views.license_detail, name='license_detail'),
    path('licenses/<int:pk>/update/', views.license_update, name='license_update'),
    path('licenses/<int:pk>/delete/', views.license_delete, name='license_delete'),
]