from django.http import HttpResponse
from django.shortcuts import render


def myfirstview(request):
    data = {
        'name': 'Javier'
    }

    return render(request, 'index.html', data)

