# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.utils.translation import ugettext_lazy as _
from reporting.reports import ReportCSVFormatter, ReportPDFFormatter, ReportGenerator, or_empty_char

from customers.models import Customer


class CustomersCSVFormatter(ReportCSVFormatter):
    filename_template = 'customers-report.csv'

    def generate_csv(self, response, customers):
        writer = self.get_csv_writer(response)
        header_row = [_('Customer Name'),
                      _('Address'),
                      _('Phone'),
                      _('Fax'),
                      _('Email'),
                      _('Contact Person'),
                      _('Notes'),]
        writer.writerow(header_row)
        for customer in customers:
            row = [or_empty_char(customer.name),
                   customer.street_line1 + ' ' + customer.street_line2 + ' , ' + customer.city + ' - ' + customer.postcode,
                   or_empty_char(customer.phone_number),
                   or_empty_char(customer.fax_number),
                   or_empty_char(customer.email),
                   or_empty_char(customer.contact_person),
                   or_empty_char(customer.notes)]
            writer.writerow(row)

    def filename(self):
        return self.filename_template

class CustomersPDFFormatter(ReportPDFFormatter):
    filename_template = 'customers-report.pdf'

    def generate_pdf(self, customers):
        context = {}
        context['customers'] = customers
        template = 'reports/customers_pdf_report.html'
        return self.render_pdf(context, template)

    def filename(self):
        return self.filename_template

class CustomersReportGenerator(ReportGenerator):
    code = 'customers'
    description = _('Customers')

    formatters = {
        'CSV_formatter': CustomersCSVFormatter,
        'PDF_formatter': CustomersPDFFormatter,
    }

    def generate(self):
        customers = Customer.objects.filter(active=True)
        return self.formatter.generate_response(customers)