from django.utils.translation import ugettext_lazy as _
from reporting.reports import ReportCSVFormatter, ReportGenerator, or_empty_char, yes_no

from vehicles.models import Vehicles


class VehiclesCSVFormatter(ReportCSVFormatter):
    filename_template = 'vehicles-report.csv'

    def generate_csv(self, response, vehicles):
        writer = self.get_csv_writer(response)
        header_row = [_('Driver Name'),
                      _('Max. Gross'),
                      _('Use a stored tare')]
        writer.writerow(header_row)
        for vehicle in vehicles:
            row = [or_empty_char(vehicle.driver_name),
                   or_empty_char(vehicle.max_gross),
                   yes_no(vehicle.use_stored_tare)]
            writer.writerow(row)

    def filename(self):
        return self.filename_template


class VehiclesReportGenerator(ReportGenerator):
    code = 'vehicles'
    description = _('Vehicles')

    formatters = {
        'CSV_formatter': VehiclesCSVFormatter,
    }

    def generate(self):
        vehicles = Vehicles.objects.filter(active=True)
        return self.formatter.generate_response(vehicles)