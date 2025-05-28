from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('recipes/<int:id>/', views.recipes, name='Recipes')
]
