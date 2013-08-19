# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
import sys, glob, inspect
import serial
from django.db import models
from base.models import ActivableMixin
from django.utils.translation import gettext as _

from django.utils.importlib import import_module

from weighin.devices import drivers

def port_list():
    """
    List ports available on machine
    """
    if sys.platform == "Win32":
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append(i)
                s.close()
            except serial.SerialException:
                pass
        return available
    elif sys.platform == "darwin":
        # Mac
        ports = glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
    else:
        # Assume Linux or something else
        i = 0
        ports = glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

    choices = tuple((str(i),ports[i]) for i in range(len(ports)))
    return choices

def drivers_list():
    """
    Get a tuple of available drivers
    """
    controllers = inspect.getmembers(drivers, inspect.isclass)
    del controllers[-1]

    driver_tuple = tuple(controllers)
    return driver_tuple


class Device(ActivableMixin):
    """
    Base model for storing devices
    """
    name = models.CharField(_('Device Name'), max_length = 100, blank = True)
    port = models.CharField(_('Port ID'), choices=port_list(), max_length = 255, blank = True)
    driver = models.CharField(_('Driver'), choices=drivers_list(), max_length=50, blank=True)
    default = models.BooleanField(_('Is Default?'), default=False)


    class Meta:
        ordering = ('-default',)
        verbose_name_plural = _('Devices')

    def __unicode__(self):
        return self.name

    def get_weight(self):
        #Load Driver
        driver_scope = 'weighin.devices.drivers.%s' % self.driver

        driver_cls = import_module(driver_scope)

        #initialize driver Class
        driver = driver_cls(self.name, self.port)

        #Return the weight
        return driver.get_weight()