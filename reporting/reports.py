# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import date
from django.http import HttpResponse
from reporting.csv_utils import CsvUnicodeWriter


def or_empty_char(value, char='-'):
    """
    Return a value or default if empty
    """
    return value or char

def yes_no(value):
    """
    Return a value or default if empty
    """
    return _('Yes') if value else _('No')

class ReportGenerator(object):
    """
    Top-level class that needs to be subclassed to provide a
    report generator.
    """
    filename_template = 'report.csv'
    mimetype = 'text/csv'
    code = ''
    description = '<insert report description>'

    def __init__(self, **kwargs):
        if 'start_date' in kwargs and 'end_date' in kwargs:
            self.start_date = kwargs['start_date']
            self.end_date = kwargs['end_date']

        self.formatter = self.formatters['%s_formatter' % kwargs['formatter']]()

    def report_description(self):
        return _('%(report_filter)s') % {
            'report_filter': self.description,
        }

    def generate(self, response):
        pass

    def filename(self):
        """
        Returns the filename for this report
        """
        return self.formatter.filename()


class ReportFormatter(object):
    def format_datetime(self, dt):
        return date(dt, 'DATETIME_FORMAT')

    def format_date(self, d):
        return date(d, 'DATE_FORMAT')

    def filename(self):
        return self.filename_template


class ReportCSVFormatter(ReportFormatter):

    def get_csv_writer(self, file_handle, **kwargs):
        return CsvUnicodeWriter(file_handle, **kwargs)

    def generate_response(self, objects, **kwargs):
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % self.filename(**kwargs)
        self.generate_csv(response, objects)
        return response