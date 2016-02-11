# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
import json

from app.models import (
    Devices
)


def func(request, device_id):
    json_data = {}
    device = Devices.objects.get(device_id=device_id)
    json_data['device_id'] = device.device_id
    json_data['red'] = device.red
    json_data['blue'] = device.blue
    json_data['green'] = device.green
    json_data['tape'] = device.tape
    return HttpResponse(json.dumps(json_data), content_type='application/json')

