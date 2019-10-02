from django.conf.urls import url
from django.urls import path, include
from events.views import IndexView
from events.events_register.views import register_event, delete_event, edit_event

app_name = 'events'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add', register_event, name='create_event'),
    path('delete/<int:pk>', delete_event, name='delete_event'),
    path('edit/<int:pk>', edit_event, name='edit_event'),

]