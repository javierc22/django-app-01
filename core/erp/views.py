from django.http import HttpResponse
from django.shortcuts import render


def myfirstview(request):
    return HttpResponse('Primera url')
