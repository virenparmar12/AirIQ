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
from django.core import serializers
# Create your views here.


def index(request):
    return render(request, 'index.html')

def getData(request):
    latest_data_id = HomeData.objects.latest('id')
    Home_data = HomeData.objects.get(id=latest_data_id.id)
    response = {}
    response["cr1"] = Home_data.cr1
    response["cr2"] = Home_data.cr2
    response["metal_loss1"] = Home_data.metal_loss1
    response["metal_loss2"] = Home_data.metal_loss2
    response["temprature"] = Home_data.temprature
    response["differential_pressure"] = Home_data.differential_pressure
    response["relative_humidity"] = Home_data.relative_humidity
    response["corrosion_rate1"] = Home_data.corrosion_rate1
    response["corrosion_rate2"] = Home_data.corrosion_rate2

    # json_data = serializers.serialize('json',HomeData.objects.filter(id=latest_data_id.id))
    # data = {'Home_data': Home_data}
    # print(json.dumps(list(Home_data))[0])

    return JsonResponse({"Home_data": response})



def every_second(request):
    pass

def air_settings(request):
    return render(request, 'settings.html')
