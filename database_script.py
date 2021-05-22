import os
import django
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AirIQ.settings')

django.setup()

from airiq_app.models import HomeData

ip_address = "127.0.0.1"

client = ModbusTcpClient(ip_address)

client.connect()

register_value_list = []
x = 40021
for i in range(7):
    read_value = client.read_holding_registers(x, 2)
    real_decoder = BinaryPayloadDecoder.fromRegisters(
        read_value.registers, byteorder=Endian.Big, wordorder=Endian.Little)
    value = real_decoder.decode_32bit_float()
    register_value_list.append(value)
    x += 2
    # print(value)
# print('%.2f' % register_value_list[4])
homedata = HomeData(
    differential_pressure='%.2f' % register_value_list[4], temprature=register_value_list[2], relative_humidity=register_value_list[3],metal_loss1=register_value_list[0],metal_loss2=register_value_list[1],cr1=register_value_list[5],cr2=register_value_list[6])
homedata.save()
