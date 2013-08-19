from django import forms
from django.utils.translation import ugettext_lazy as _
from reporting.utils import ReportList

class ReportForm(forms.Form):
    """
    Form to generate reports
    """
    generators = ReportList().get_report_generators()

    type_choices = []
    formats = [('CSV', 'CSV')]
    for generator in generators:
        type_choices.append((generator.code, generator.description))

    report_type = forms.ChoiceField(widget=forms.Select(), choices=type_choices, label=_("Report Type"))
    report_format = forms.ChoiceField(widget=forms.Select(), choices=formats, label=_("File Format"))