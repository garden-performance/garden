from __future__ import unicode_literals

from django.db import models


class Devices(models.Model):
    """docstring for device"""
    device_id = models.IntegerField()
    red = models.BooleanField(default=True)
    blue = models.BooleanField(default=True)
    green = models.BooleanField(default=True)
    tape = models.BooleanField(default=True)
