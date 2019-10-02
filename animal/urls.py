from django.urls import path
from animal.views import (animal, new_animal, update_animal, del_animal, new_species_popup, new_breed_popup,
                          new_clinical_log, update_clinical_log, del_clinical_log, new_shelter, update_shelter, del_shelter, )


app_name = 'animals'

urlpatterns = [
    path('', animal, name='home'),
    path('add/animal', new_animal, name='create_animal'),
    path('edit/animal/<int:pk>', update_animal, name='edit_animal'),
    path('delete/animal/<int:pk>', del_animal, name='delete_animal'),

    path('add/species', new_species_popup, name='create_species'),
    path('add/breed', new_breed_popup, name='create_breed'),

    path('add/clinical_log/<int:pk>', new_clinical_log, name='create_clinical_log'),
    path('edit/clinical_log/<int:pk>', update_clinical_log, name='edit_clinical_log'),
    path('delete/clinical_log/<int:pk>', del_clinical_log, name='delete_clinical_log'),

    path('add/shelter/<int:pk>', new_shelter, name='create_shelter'),
    path('edit/shelter/<int:pk>', update_shelter, name='edit_shelter'),
    path('delete/shelter/<int:pk>', del_shelter, name='delete_shelter'),
]
