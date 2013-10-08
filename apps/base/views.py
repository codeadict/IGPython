# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from ast import literal_eval

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django import http
from django.views import generic
from django.utils import simplejson
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.contrib import messages

from base.models import Setting
from weighin.models import Device
from products.models import Category, EWC
from base.forms import SettingsForm

@login_required
@require_http_methods(['GET', 'POST'])
def edit_settings(request):
    """Edit system settings"""
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.save_settings()
            messages.info(request, _(u'System settings have been saved.'))
            return HttpResponseRedirect(reverse('configure'))
        # Invalid form
        return render_to_response("settings.html", {'form': form, 'settings_tab': True}, context_instance=RequestContext(request))

    # Pass the current settings as the initial values.
    values = Setting.objects.all().values()
    initial = dict()
    for v in values:
        try:
            # Uses ast.literal_eval to convert 'False' => False etc.
            initial[v['name']] = literal_eval(v['value'])
        except (SyntaxError, ValueError):
            # Attempted to convert the string value to a Python value
            # but failed so leave it a string.
            initial[v['name']] = v['value']
    form = SettingsForm(initial=initial)
    return render_to_response("settings.html", {'form': form, 'settings_tab': True}, context_instance=RequestContext(request))


@login_required
def base_data(request):
    ewc = EWC.objects.all()
    categories = Category.objects.all()

    return render_to_response("base/basedata/index.html",
        {'categories': categories,
         'ewc': ewc,
         'basedata_tab': True},
        context_instance=RequestContext(request))


class UsersList(generic.ListView):
    template_name = 'base/users/index.html'
    context_object_name = "operators"
    model = User

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(UsersList, self).get_context_data(**kwargs)
        context['operators_tab'] = True
        return context

class DeviceList(generic.ListView):
    template_name = 'base/devices/index.html'
    context_object_name = "devices"
    model = Device

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(DeviceList, self).get_context_data(**kwargs)
        context['devices_tab'] = True
        return context


