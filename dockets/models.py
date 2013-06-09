from django.db import models


from django.utils.translation import gettext as _


class Docket(models.Model):
    """
    Dockets Model
    """
    docket_number = models.IntegerField(verbose_name=_('Docket No.'))
    docket_date = models.DateField(auto_now_add=True, verbose_name=_('Docket Date'))
    
    gross = models.DecimalField(max_digits=14, decimal_places=6, verbose_name=_('Gross'))
    tare = models.DecimalField(max_digits=14, decimal_places=6, verbose_name=_('Tare'))
    ind_id = models.IntegerField(max_length = 4, verbose_name=_('Ind ID'))
    ind_id2 = models.IntegerField(max_length = 4, verbose_name=_('Ind ID'))
    
    cancelled = models.BooleanField(_('Cancelled'))
    
    class Meta:
        ordering = ('docket_date',)
        verbose_name_plural = _('Dockets')
        
    def net(self):
        """
        Returns the net weigh
        net = gross - tare
        """
        return self.gross - self.tare
    
    
