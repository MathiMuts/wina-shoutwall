# shoutwall/urls.py

from django.urls import path
from . import views

app_name = 'shoutwall'

urlpatterns = [
    path('', views.index, name='index'),
]