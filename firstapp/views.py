from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def first(request):
    return render(request, '1.html')


def third(request):
    return render(request, '3.html')
