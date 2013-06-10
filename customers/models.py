from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from phonenumber_field.modelfields import PhoneNumberField

from base.models import ActivableMixin

from django.utils.safestring import mark_safe


class Customer(ActivableMixin):
    name = models.CharField(max_length=255, verbose_name=_('Customer Name'))
    
    #adresss
    street_line1 = models.CharField(_('Address 1'), max_length = 100, blank = True)
    street_line2 = models.CharField(_('Address 2'), max_length = 100, blank = True)
    city = models.CharField(_('City'), max_length = 100, blank = True)
    postcode = models.CharField(_('Post code'), max_length = 5, blank = True)
    
    phone_number = PhoneNumberField(_('Phone'))
    fax_number = PhoneNumberField(_('Fax'), null=True, blank=True)
    email = models.EmailField(blank=True)
    contact_person = models.CharField(max_length=255, verbose_name=_('Contact Person'))
    requires_reference = models.BooleanField(_('Requires reference number?'))
    notes = models.TextField(_('Notes'))
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = _('Customers')
        
    def image_or_default(self):
        """Return user company or a default."""
        avatar = '%s%s' % (settings.STATIC_URL, '/img/customer-missing.jpg')
        
#         if self.image:
#             avatar = '%s%s' % (settings.MEDIA_URL, self.image)
            
        return mark_safe(avatar)
