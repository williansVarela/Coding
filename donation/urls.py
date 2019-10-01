from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation_list, name='donation_list'),
    path('<int:pk>/', views.donation_detail, name='donation_detail'),
    path('new/', views.donation_new, name='donation_new'),
    path('<int:pk>/edit/', views.donation_edit, name='donation_edit'),
    path('donation_delete/<int:pk>/', views.donation_delete, name='donation_delete'),
]