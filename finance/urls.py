from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('<int:pk>/', views.expense_detail, name='expense_detail'),
    path('new/', views.expense_new, name='expense_new'),
    path('<int:pk>/edit/', views.expense_edit, name='expense_edit'),
    path('expense_delete/<int:pk>/', views.expense_delete, name='expense_delete'),
]