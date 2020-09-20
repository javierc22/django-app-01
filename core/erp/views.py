from django.http import HttpResponse
from django.shortcuts import render
from core.erp.models import Category


def myfirstview(request):
    data = {
        'name': 'Javier',
        'categories': Category.objects.all()
    }

    return render(request, 'home.html', data)

