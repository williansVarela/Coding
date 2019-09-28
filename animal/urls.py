from django.urls import path
from animal.views import (animal,
                          new_animal,
                          update_animal,
                          del_animal,
                          new_species_popup,
                          new_breed_popup,
                          new_health_popup,
                          new_healthlog_popup,
                          shelter,
                          new_shelter,
                          update_shelter,
                          del_shelter,)

urlpatterns = [
    path('list_animals/', animal, name='animal'),
    path('new_animal/', new_animal, name='new_animal'),
    path('update_animal/<int:pk>/', update_animal, name='update_animal'),
    path('del_animal/<int:pk>/', del_animal, name='del_animal'),
    path('new_species/', new_species_popup, name='new_species_popup'),
    path('new_breed/', new_breed_popup, name='new_breed_popup'),
    path('new_health/', new_health_popup, name='new_health_popup'),
    path('new_healthlog/<int:pk>/', new_healthlog_popup, name='new_healthlog_popup'),

    path('list_shelters/', shelter, name='shelter'),
    path('new_shelter/', new_shelter, name='new_shelter'),
    path('update_shelter/<int:pk>/', update_shelter, name='update_shelter'),
    path('del_shelter/<int:pk>/', del_shelter, name='del_shelter'),
]
