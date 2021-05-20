from django.http import request
from django.shortcuts import render
from airiq_app.models import *
# Create your views here.


def index(request):
    data = HomeData.objects.first()
    return render(request, 'index.html', {'data': data})


def air_settings(request):
    return render(request, 'settings.html')
