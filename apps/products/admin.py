# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.contrib import admin

from products.models import (Category, EWC, Product)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 10

class EWCAdmin(admin.ModelAdmin):
    list_display = ('code', 'description',)
    list_per_page = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ('active', 'code', 'name', 'category', )
    list_filter = ('active', 'category__name',)
    list_per_page = 10

#Register  Admin Interfaces
admin.site.register(Category, CategoryAdmin)
admin.site.register(EWC, EWCAdmin)
admin.site.register(Product, ProductAdmin)