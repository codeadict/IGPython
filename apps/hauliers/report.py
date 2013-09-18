# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.utils.translation import ugettext_lazy as _
from reporting.reports import ReportCSVFormatter, ReportPDFFormatter, ReportGenerator, or_empty_char, yes_no

from hauliers.models import Haulier


class HauliersCSVFormatter(ReportCSVFormatter):
    filename_template = 'hauliers-report.csv'

    def generate_csv(self, response, hauliers):
        writer = self.get_csv_writer(response)
        header_row = [_('Haulier Name'),
                      _('Address'),
                      _('Phone'),
                      _('Fax'),
                      _('Email'),
                      _('Contact Person'),
                      _('Notes'),]
        writer.writerow(header_row)
        for haulier in hauliers:
            row = [or_empty_char(haulier.name),
                   haulier.street_line1 + ' ' + haulier.street_line2 + ' , ' + haulier.city + ' - ' + haulier.postcode,
                   or_empty_char(haulier.phone_number),
                   or_empty_char(haulier.fax_number),
                   or_empty_char(haulier.email),
                   or_empty_char(haulier.contact_person),
                   or_empty_char(haulier.notes)]
            writer.writerow(row)

    def filename(self):
        return self.filename_template
    
class HauliersPDFFormatter(ReportPDFFormatter):
    filename_template = 'hauliers-report.pdf'

    def generate_pdf(self, hauliers):
        context = {}
        context['hauliers'] = hauliers
        template = 'reports/hauliers_pdf_report.html'
        return self.render_pdf(context, template)

    def filename(self):
        return self.filename_template


class HauliersReportGenerator(ReportGenerator):
    code = 'hauliers'
    description = _('Hauliers')

    formatters = {
        'CSV_formatter': HauliersCSVFormatter,
        'PDF_formatter': HauliersPDFFormatter,
    }

    def generate(self):
        hauliers = Haulier.objects.filter(active=True)
        return self.formatter.generate_response(hauliers)