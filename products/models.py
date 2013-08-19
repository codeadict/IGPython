# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.db import models
from base.models import ActivableMixin
from django.utils.translation import gettext as _


class Category(models.Model):
    """
    Product Categories
    """
    name = models.CharField(_('Category Name'), max_length=255, db_index=True)

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

    def __unicode__(self):
        return self.name

class EWC(models.Model):
    """
    Table of European Waste Codes
    """
    code = models.CharField(_('Code'), max_length=10, unique=True)
    description = models.CharField(max_length=255, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('European Waste Code')
        verbose_name_plural = _('European Waste Codes')

    def __unicode__(self):
        return u'%s - %s' % (self.code, self.description)

class Product(ActivableMixin):
    """
    Base Products Class
    """
    code = models.CharField(_('Product Code'), max_length=64, unique=True)
    name = models.CharField(max_length=255, verbose_name=_('Product Name'))
    description = models.TextField(verbose_name=_('Product Description'), null=True, blank=True)

    category = models.ForeignKey('products.Category', verbose_name=_('Product Category'))
    ewc = models.ForeignKey('products.EWC', verbose_name=_('Product EWC'))

    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return u'%s - %s' % (self.code, self.name)




