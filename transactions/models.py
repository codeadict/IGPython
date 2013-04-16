from django.db import models
from django.utils.translation import gettext as _

class Transaction(models.Model):
    '''
    Base model for weight transaction 
    '''
    ticket_number = models.IntegerField(_('Ticket Number'))
    date_time_in = models.DateTimeField(_('Date/Time In'))
    date_time_out = models.DateTimeField(_('Date/Time Out'))
    
