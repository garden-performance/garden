#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from app.models import (
    Devices
)

from app.aggregate import (
    get_all_device_info
)


def set_light(request, name):
    try:
        return request.POST[name]
    except:
        return 0


@login_required
def home(request):
    if request.method == 'POST':
        device_id = request.POST['device_id']
        red = set_light(request, 'red')
        blue = set_light(request, 'blue')
        green = set_light(request, 'green')
        tape = set_light(request, 'tape')
        default = dict(
            red=red,
            blue=blue,
            green=green,
            tape=tape
        )
        created = Devices.objects.filter(device_id=device_id).count()
        if created != 0:
            Devices.objects.filter(device_id=device_id).update(
                device_id=device_id,
                red=red,
                green=green,
                blue=blue,
                tape=tape
            )
        else:
            device_objects = Devices(
                device_id=device_id,
                red=red,
                blue=blue,
                green=green,
                tape=tape
            )
            device_objects.save()
    data = {"url": "register"}
    return render(request, 'app/index.html', data)


@login_required
def manage(request):
    devices = get_all_device_info()
    state = []
    for device in devices:
        tmp = {}
        tmp['device'] = device[1]
        tmp['red'] = device[2]
        tmp['blue'] = device[3]
        tmp['green'] = device[4]
        tmp['tape'] = device[5]
        state.append(tmp)
    print state
    data = {"url": "manage", "state": state}
    return render(request, 'app/manage.html', data)
