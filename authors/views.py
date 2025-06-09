from django.http import Http404
from django.shortcuts import render

from authors.forms import RegisterForm

# Create your views here.


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()
    else:
        form = RegisterForm(request.POST)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })
