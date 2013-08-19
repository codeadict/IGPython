# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.conf import settings
import hashlib
from django.db import models

from django.utils.translation import gettext as _


class Docket(models.Model):
    """
    Dockets Model
    """
    docket_number = models.IntegerField(verbose_name=_('Docket No.'), db_index=True, unique=True)
    docket_date = models.DateField(auto_now_add=True, verbose_name=_('Docket Date'))
    
    gross = models.DecimalField(max_digits=14, decimal_places=6, verbose_name=_('Gross'))
    tare = models.DecimalField(max_digits=14, decimal_places=6, verbose_name=_('Tare'))
    ind_id = models.IntegerField(max_length=4, verbose_name=_('Ind ID'))
    ind_id2 = models.IntegerField(max_length=4, verbose_name=_('Ind ID'))
    
    cancelled = models.BooleanField(_('Cancelled'))
    
    class Meta:
        ordering = ('-docket_date',)
        verbose_name_plural = _('Dockets')
        permissions = (
            ("can_correct", _("Can correct Dockets(Modify It)"))
        )

    def __unicode__(self):
        return u"#%s" % self.docket_number

    def verification_hash(self):
        return hashlib.md5('%s%s' % (self.docket_number, settings.SECRET_KEY)).hexdigest()

    @property
    def net(self):
        """
        Returns the net weigh
        net = gross - tare
        """
        return self.gross - self.tare