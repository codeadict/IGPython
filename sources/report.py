from django.utils.translation import ugettext_lazy as _
from reporting.reports import ReportCSVFormatter, ReportGenerator, or_empty_char, yes_no

from sources.models import LoadingPoint


class SourcesCSVFormatter(ReportCSVFormatter):
    filename_template = 'sources-report.csv'

    def generate_csv(self, response, lps):
        writer = self.get_csv_writer(response)
        header_row = [_('Loading Point'),
                      _('Taken from Loading Point'),
                      _('Is a Destination?'),]
        writer.writerow(header_row)
        for lp in lps:
            row = [or_empty_char(lp.name),
                   or_empty_char(lp.ammount_taken),
                   yes_no(lp.is_destination)]
            writer.writerow(row)

    def filename(self):
        return self.filename_template

class SourcesReportGenerator(ReportGenerator):
    code = 'sources'
    description = _('Loading Points')

    formatters = {
        'CSV_formatter': SourcesCSVFormatter,
    }

    def generate(self):
        lp = LoadingPoint.objects.filter(active=True)
        return self.formatter.generate_response(lp)