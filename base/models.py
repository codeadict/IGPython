from django.db import models
from django.utils.translation import gettext as _


class ActivableMixin(models.Model):
    active = models.BooleanField(verbose_name=_('Active'))

    class Meta:
        abstract = True
