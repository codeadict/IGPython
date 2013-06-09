from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

class TextInputAppend(forms.TextInput):
    
    def __init__(self, *args, **kwargs):
        self.prepend = kwargs.pop('prepend', "")
        super(TextInputAppend, self).__init__(*args, **kwargs)
    
    def render(self, *args, **kwargs):
        html = super(TextInputAppend, self).render(*args, **kwargs)
        return mark_safe('<div class="input-append">%s<span class="add-on btn">%s</span></div>' % (html, self.prepend))


class CreateVehicle(forms.Form):
    
    def __init__(self, request, *args, **kwargs):
        super(CreateVehicle, self).__init__(*args, **kwargs)
        self.request = request
    
    driver_name = forms.CharField(label=_(u'Driver Name'),)
    max_gross = forms.DecimalField(label=_(u'Max Gross'), help_text=_('Max gross the vehicle can charge'))
    
    use_stored_tare = forms.BooleanField(label=_(u'Use a Stored Tare'), required=False)
    print_ticket = forms.BooleanField(label=_(u'Print Ticket'), required=False)
    reference_number = forms.BooleanField(label=_(u'Vehicle reference number'), required=False)
    active = forms.BooleanField(label=_(u'Active'), required=False)
    
    def clean(self):
        return self.cleaned_data