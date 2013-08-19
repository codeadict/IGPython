from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Transaction(models.Model):
    """
    Base model for weight transaction 
    """
    device = models.ForeignKey('weighin.Device', verbose_name=_('Select Weighbridge'))
    ticket_number = models.IntegerField(_('Ticket Number'))
    date_time_in = models.DateTimeField(_('Date/Time In'))
    date_time_out = models.DateTimeField(_('Date/Time Out'))
    vehicle = models.ForeignKey('vehicles.Vehicles', related_name='transactions', verbose_name=_('Vehicle Registration'))
    loading_point = models.ForeignKey('sources.LoadingPoint', verbose_name=_('Loading Point'))
    product = models.ForeignKey('products.Product', verbose_name=_('Product'))
    operator = models.ForeignKey(User, verbose_name=_('Operator'))
    client = models.ForeignKey('customers.Customer', verbose_name=_('Client'))

    class Meta:
        ordering = ('date_time_in',)
        verbose_name_plural = _('Transactions')

    def __unicode__(self):
        return str(self.ticket_number)


    def product_category(self):
        return self.product.category.name
    
