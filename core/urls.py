"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from core.views import (LoginView, HomeView, register_user, change_password, UpdateProfile, list_users, disable_user,
                        active_user, delete_user)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('user/disable/<int:pk>', disable_user, name='disable_user'),
    path('user/active/<int:pk>', active_user, name='active_user'),
    path('user/delete/<int:pk>', delete_user, name='delete_user'),

    path('animals/', include('animal.urls')),
    path('contacts/', include('contacts.urls')),
    path('dashboard/', include('dashboard.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url('login/', LoginView.as_view(), name='login'),
    url(r'user/register/$', register_user, name='create_user'),
    url(r'user/all/$', list_users, name='list_users'),
    url(r'user/password/$', change_password, name='change_password'),
    url(r'profile/update/$', UpdateProfile.as_view(), name='update_profile'),

]
