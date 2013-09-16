# -*- coding: utf-8 -*-
import os
from cStringIO import StringIO
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import date
from django.http import HttpResponse
from django.template import Context, RequestContext
from django.template.loader import render_to_string
from reporting.csv_utils import CsvUnicodeWriter

from xhtml2pdf import pisa


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

class ReportPDFFormatter(ReportFormatter):
    """
    PDF report formatter
    """
    pdfresponse = None

    def fetch_resources(self, uri, rel):
        """
        Callback to allow pisa/reportlab to retrieve images, stylesheets, etc.
        """
        return os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))

    def render_pdf(self, context, tpl):
        encoding = "UTF-8"
        content = render_to_string(tpl, context)
        src = StringIO(content.encode(encoding))
        out = StringIO()
        result = pisa.CreatePDF(src, out, link_callback=self.fetch_resources, encoding="UTF-8")
        print "PDF Generated"
        if not result.err:
            self.pdfresponse = out.getvalue()
            return out.getvalue()
        else:
            print "Error on PDF"

    def generate_response(self, objects, **kwargs):
        response = HttpResponse(self.generate_pdf(objects), mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=%s' % self.filename(**kwargs)
        return response

