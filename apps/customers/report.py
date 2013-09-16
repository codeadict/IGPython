from django.utils.translation import ugettext_lazy as _
from reporting.reports import ReportCSVFormatter, ReportGenerator, or_empty_char

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

class CustomersReportGenerator(ReportGenerator):
    code = 'customers'
    description = _('Customers')

    formatters = {
        'CSV_formatter': CustomersCSVFormatter,
    }

    def generate(self):
        customers = Customer.objects.filter(active=True)
        return self.formatter.generate_response(customers)