# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import ModelForm

from vehicles.models import Vehicles

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('reference_number', 'driver_name', 'max_gross', 'use_stored_tare', 'print_ticket')
    list_per_page = 10
    
    
admin.site.register(Vehicles, VehiclesAdmin)