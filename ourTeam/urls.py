from django import views
from django.urls import path
from ourTeam import views
urlpatterns = [
    path('', views.team, name='team'),
]