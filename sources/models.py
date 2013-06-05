from django.db import models
from django.utils.translation import gettext as _

from base.models import ActivableMixin


class LoadingPoint(ActivableMixin):
    name = models.CharField(max_length=255, verbose_name=_('Loading Point'))
    ammount_taken = models.DecimalField(max_digits=14, decimal_places=6, verbose_name=_('Taken from Loading Point'))
    
    
    is_destination = models.BooleanField(_('Is a Destination?'))
    requires_reference = models.BooleanField(_('Requires reference number?'))
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = _('Loading Ponts')
        
    def reset_total(self):
        """
        Resets the total of Ton. Taken
        """
        pass
