# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.contrib import admin

from weighin.models import Device

class DevicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'port', 'default')
    list_per_page = 10

admin.site.register(Device, DevicesAdmin)