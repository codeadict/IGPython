# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django import http
from django.conf import settings as django_settings
from django.contrib import admin
from django.shortcuts import render
from django.template import RequestContext
from django.views import debug

def settings(request):
    """Admin view that displays the django settings."""
    settings = debug.get_safe_settings()
    sorted_settings = [{'key': key, 'value': settings[key]} for
                       key in sorted(settings.keys())]

    return render('base/settings.html',
                              {'settings': sorted_settings,
                               'title': 'Settings'},
                              RequestContext(request, {}))

admin.site.admin_view(settings)