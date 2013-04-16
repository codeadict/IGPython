from django.db import models
from django.utils.translation import gettext as _


class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Customer Name'))
    email = models.EmailField(blank=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = _('Customers')
