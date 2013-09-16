# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django import forms
from django.utils.translation import ugettext as _

from hauliers.models import Haulier



class CreateHaulier(forms.ModelForm):

    class Meta:
        model = Haulier