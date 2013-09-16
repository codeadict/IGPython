# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django import forms
from django.db.models import get_model

from django.utils.translation import ugettext_lazy as _

Product = get_model('products', 'Product')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('date_created',)