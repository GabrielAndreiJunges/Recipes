from django.shortcuts import render
from django.urls import path


def register_view(request):
    render(request, 'authors/pages/register_view.html')
