from django.db import models
from django.utils.translation import gettext as _

from base.models import ActivableMixin


class Vehicles(ActivableMixin):
    """
    Database model for vehicles.
    """
    driver_name = models.CharField(max_length=255, verbose_name=_('Drivers Name'))
    max_gross = models.DecimalField(max_digits=14, decimal_places=6, verbose_name=_('Max. Gross'))
    
    use_stored_tare = models.BooleanField(verbose_name=_('Use a stored tare'))
    print_ticket = models.BooleanField(verbose_name=_('Print ticket'))
    reference_number = models.BooleanField(verbose_name=_('Vehicle reference number'))
    
    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

