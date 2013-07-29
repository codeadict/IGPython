import sys, glob
import serial
from django.db import models
from base.models import ActivableMixin
from django.utils.translation import gettext as _

# Create your models here.

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
        return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
    else:
        # Assume Linux or something else
        return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

class Devices(ActivableMixin):
    """
    Base model for storing devices
    """
    name = models.CharField(_('Device Name'), max_length = 100, blank = True)
    port = models.CharField(_('Port ID'), max_length = 255, blank = True)