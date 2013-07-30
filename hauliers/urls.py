# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.conf.urls import patterns, include, url
from hauliers.views import HauliersList, HaulierCreate
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(HauliersList.as_view()), name='haulier_list'),
    url('^create/$', HaulierCreate.as_view(), name='haulier_create'),
)