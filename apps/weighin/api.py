# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization

from transactions.models import Transaction
from vehicles.models import Vehicles
from products.models import Product


class VehicleResource(ModelResource):
    class Meta:
        queryset = Vehicles.objects.all()
        resource_name = 'vehicle'

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'

class TransactionResource(ModelResource):
    vehicle = fields.ForeignKey(VehicleResource, 'vehicle', full=True)
    product = fields.ForeignKey(ProductResource, 'product', full=True)

    class Meta:
        queryset = Transaction.objects.all()
        resource_name = 'item'
        fields = ['vehicle', 'product', 'date_time_in', 'date_time_out', 'order_number']
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete', 'put']
        always_return_data = True