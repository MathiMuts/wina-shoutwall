# pauze/urls.py

from django.urls import path
from . import views

app_name = 'pauze'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/data/', views.pauze_api, name='api'),
]