# -*- coding: utf-8 -*-#
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import ModelForm

from customers.models import Customer

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'contact_person')
    list_per_page = 10
    
    
admin.site.register(Customer, CustomersAdmin)

