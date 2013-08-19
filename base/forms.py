from django import forms
from django.utils.translation import ugettext as _
from django.conf import settings

from base.models import Configuration


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Configuration
        fields = ('company_name', 'street1', 'street2', 'city', 'state', 'postcode' )


class CompanyLogoForm(forms.ModelForm):

    class Meta:
        model = Configuration
        fields = ('logo',)

    def clean_logo(self):
        if self.cleaned_data['logo'].size > settings.MAX_IMAGE_SIZE:
            max_size = settings.MAX_IMAGE_SIZE / 1024
            msg = _("Image exceeds max image size: %(max)dk")
            raise forms.ValidationError(msg % dict(max=max_size))
        return self.cleaned_data['logo']