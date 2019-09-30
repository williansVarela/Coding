from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from dashboard.views import IndexView

app_name = 'dashboard'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]

