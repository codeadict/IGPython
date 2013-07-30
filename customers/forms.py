from django import forms
from django.utils.translation import ugettext as _

from customers.models import Customer



class CreateCustomer(forms.ModelForm):

    class Meta:
        model = Customer
