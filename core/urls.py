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
from core.views import LoginView, HomeView, register_user, change_password, UpdateProfile, list_users, desable_user, active_user
from animal.views import (animal,
                          new_animal,
                          update_animal,
                          del_animal,
                          new_species_popup,
                          new_breed_popup,
                          new_health_popup,
                          shelter,
                          new_shelter,
                          update_shelter,
                          del_shelter,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('user/desable/<int:pk>', desable_user, name='desable_user'),
    path('user/active/<int:pk>', active_user, name='active_user'),

    url(r'^$', HomeView.as_view(), name='home'),
    url('login/', LoginView.as_view(), name='login'),
    url(r'user/register/$', register_user, name='create_user'),
    url(r'user/all/$', list_users, name='list_users'),
    url(r'user/password/$', change_password, name='change_password'),
    url(r'profile/update/$', UpdateProfile.as_view(), name='update_profile'),

    path('animal/', animal, name='animal'),
    path('new_animal/', new_animal, name='new_animal'),
    path('update_animal/<int:pk>', update_animal, name='update_animal'),
    path('del_animal/<int:pk>', del_animal, name='del_animal'),
    path('species/create', new_species_popup, name='new_species_popup'),
    path('breed/create', new_breed_popup, name='new_breed_popup'),
    path('health/create', new_health_popup, name='new_health_popup'),

    path('shelter/', shelter, name='shelter'),
    path('new_shelter/', new_shelter, name='new_shelter'),
    path('update_shelter/<int:pk>', update_shelter, name='update_shelter'),
    path('del_shelter/<int:pk>', del_shelter, name='del_shelter'),
]
