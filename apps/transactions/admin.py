# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.contrib import admin

from transactions.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'date_time_in', 'date_time_out', 'vehicle', 'operator', 'client', )
    list_filter = ('date_time_in', 'date_time_out', 'operator__username', 'client__name',)
    list_per_page = 10

#Register  Admin Interfaces
admin.site.register(Transaction, TransactionAdmin)