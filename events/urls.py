from django.conf.urls import url
from django.urls import path, include
from events.views import IndexView, register_event, delete_event

app_name = 'events'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add', register_event, name='create_event'),
    path('delete/<int:pk>', delete_event, name='delete_event'),

]