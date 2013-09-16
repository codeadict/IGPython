# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django import forms
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy
from django.conf import settings

from base.models import Setting


class SettingsForm(forms.Form):
    """
    Form to Edit Global Settings
    """
    company_name = forms.CharField(
        required=False, initial='Your Company',
        label=_lazy(u'Company Name'))
    logo = forms.ImageField(
        required=False,
        label=_lazy(u'Company Logo'))
    street1 = forms.CharField(
        required=False,
        label=_lazy(u'Address 1'))
    street2 = forms.CharField(
        required=False,
        label=_lazy(u'Address 2'))
    city = forms.CharField(
        required=False,
        label=_lazy(u'City'))
    state = forms.CharField(
        required=False,
        label=_lazy(u'State/County'))
    postcode = forms.CharField(
        required=False,
        label=_lazy(u'Post/Zip-code'))
    
    def save_settings(self):
        for field in self.fields.keys():
            value = str(self.cleaned_data[field])
            setting = Setting.objects.filter(name=field)
            update_count = setting.update(value=value)
            if update_count == 0:
                # This user didn't have this setting so create it.
                Setting.objects.create(name=field, value=value)
                