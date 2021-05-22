from django.db.models.fields import json
from django.http import request,JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from airiq_app.models import *
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
from airiq_app.models import *
from django.forms.models import model_to_dict
import json
# Create your views here.


def index(request):
    return render(request, 'index.html')

def getData(request):
    Home_data = HomeData.objects.all()[:20]
    return JsonResponse({"Home_data":list(Home_data.values())[-1]})

def air_settings(request):
    return render(request, 'settings.html')
