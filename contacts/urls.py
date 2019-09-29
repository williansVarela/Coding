from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from contacts.views import IndexView
from contacts.contacts_register.views import register_contact, delete_contact, edit_contact

app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add', register_contact, name='create_contact'),
    path('delete/<int:pk>', delete_contact, name='delete_contact'),
    path('update/<int:pk>', edit_contact, name='edit_contact'),
]
