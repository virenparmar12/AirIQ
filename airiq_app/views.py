from django.http import request
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def air_settings(request):
    return render(request, 'settings.html')