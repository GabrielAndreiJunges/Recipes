from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Otávio',
    })


def sobre(request):
    return render(request, 'recipes/sobre.html')


def contato(request):
    return render(request, 'recipes/contato.html')
