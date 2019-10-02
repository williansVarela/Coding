from django.conf.urls import url
from django.urls import path, include
from events.views import IndexView

app_name = 'events'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),

]