# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.conf.urls import patterns, include, url
from hauliers.views import HauliersList, HaulierView, HaulierCreate, HaulierUpdate, delete_haulier
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(HauliersList.as_view()), name='haulier_list'),
    url('^(?P<pk>\d+)/$', HaulierView.as_view(), name='haulier_details'),
    url('^create/$', HaulierCreate.as_view(), name='haulier_create'),
    url(r'^(?P<pk>\d+)/update/$', HaulierUpdate.as_view(), name='haulier_update'),
    url(r'^(?P<haulier_id>\d+)/delete/$', delete_haulier, name='haulier_delete'),
)