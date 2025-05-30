from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

from . import views

# recipes:recipe ou recipes:home
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipe'),
    path('recipes/category/<int:category_id>/',
         views.category, name='category'),
]
