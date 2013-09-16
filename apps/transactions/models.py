# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from weighin.models import Device
from dockets.models import Docket


class Transaction(models.Model):
    """
    Base model for weight transaction 
    """
    device = models.ForeignKey('weighin.Device', verbose_name=_('Select Weighbridge'))
    order_number = models.IntegerField(_('Order Number'))
    date_time_in = models.DateTimeField(_('Date/Time In'), auto_now_add=True)
    date_time_out = models.DateTimeField(_('Date/Time Out'), null=True, blank=True)
    vehicle = models.ForeignKey('vehicles.Vehicles', related_name='transactions', verbose_name=_('Vehicle Registration'))
    loading_point = models.ForeignKey('sources.LoadingPoint', verbose_name=_('Loading Point'))
    product = models.ForeignKey('products.Product', verbose_name=_('Product'))
    operator = models.ForeignKey(User, verbose_name=_('Operator'), null=True, blank=True)
    client = models.ForeignKey('customers.Customer', verbose_name=_('Client'))

    class Meta:
        ordering = ('date_time_in',)
        verbose_name_plural = _('Transactions')

    def __unicode__(self):
        return str(self.order_number)
    
    @property
    def product_category(self):
        return self.product.category.name
    
    
#Signals

def post_transaction_save(sender, **kwargs):
    """
    Generate a Ticket on Transaction save
    """
    instance = kwargs.get('instance', None)
    created = kwargs.get('created', False)
    weight = instance.device.weight       
    ticket = Docket(docket_number=instance.order_number, gross=weight, tare=weight, ind_id=1, ind_id2=2, cancelled=True)
    
    ticket.save()
        

post_save.connect(post_transaction_save, sender=Transaction,
                  dispatch_uid='signal_post_transaction_save')
