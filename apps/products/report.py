from django.utils.translation import ugettext_lazy as _
from reporting.reports import ReportCSVFormatter, ReportPDFFormatter, ReportGenerator, or_empty_char

from products.models import Product


class ProductsCSVFormatter(ReportCSVFormatter):
    filename_template = 'products-report.csv'

    def generate_csv(self, response, products):
        writer = self.get_csv_writer(response)
        header_row = [_('Product Code'),
                      _('Product Name'),
                      _('Product Description'),
                      _('Product Category'),
                      _('Product EWC')]
        writer.writerow(header_row)
        for product in products:
            row = [or_empty_char(product.code),
                   or_empty_char(product.name),
                   or_empty_char(product.description),
                   or_empty_char(product.category.name),
                   or_empty_char(product.ewc)]
            writer.writerow(row)

    def filename(self):
        return self.filename_template

class ProductsPDFFormatter(ReportPDFFormatter):
    filename_template = 'products-report.pdf'

    def generate_pdf(self, products):
        context = {}
        context['products'] = products
        template = 'reports/products_pdf_report.html'
        return self.render_pdf(context, template)

    def filename(self):
        return self.filename_template



class ProductReportGenerator(ReportGenerator):
    code = 'products'
    description = _('Active Products')

    formatters = {
        'CSV_formatter': ProductsCSVFormatter,
        'PDF_formatter': ProductsPDFFormatter,
    }

    def generate(self):
        products = Product._default_manager.all()
        return self.formatter.generate_response(products)