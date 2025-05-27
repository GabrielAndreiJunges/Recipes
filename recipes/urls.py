from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

from .views import home, sobre, contato

urlpatterns = [
    path('', home, name='Home'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
]
