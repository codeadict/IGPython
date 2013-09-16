from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from vehicles.models import Vehicles

class TextInputAppend(forms.TextInput):
    
    def __init__(self, *args, **kwargs):
        self.prepend = kwargs.pop('prepend', "")
        super(TextInputAppend, self).__init__(*args, **kwargs)
    
    def render(self, *args, **kwargs):
        html = super(TextInputAppend, self).render(*args, **kwargs)
        return mark_safe('<div class="input-append">%s<span class="add-on btn">%s</span></div>' % (html, self.prepend))


class CreateVehicle(forms.ModelForm):
    max_gross = forms.CharField(widget=TextInputAppend(prepend='T'))
    
    class Meta:
        model = Vehicles