from django import forms
from transactions.models import Transaction
from weighin.models import Device

class TransactionForm(forms.ModelForm):
    """
    Form for weigh transaction
    """

    class Meta:
        model = Transaction
        fields = ('device', 'vehicle', 'loading_point', 'product', 'client')

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        default_device = None
        count = Device.objects.count()
        if count > 1:
            default_device = Device.objects.filter(default=True)[0]
        elif count == 1:
            default_device = Device.objects.all()[0]
        if default_device:
            self.initial['device'] = default_device.id
            self.fields['device'].widget=forms.HiddenInput()