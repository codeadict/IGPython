from customers.report import CustomersReportGenerator
from products.report import ProductReportGenerator
from sources.report import SourcesReportGenerator
from hauliers.report import HauliersReportGenerator
from vehicles.report import VehiclesReportGenerator


class ReportList(object):

    generators = [ProductReportGenerator,
                  CustomersReportGenerator,
                  VehiclesReportGenerator,
                  HauliersReportGenerator,
                  SourcesReportGenerator]

    def get_report_generators(self):
        return self.generators

    def get_generator(self, code):
        for generator in self.generators:
            if generator.code == code:
                return generator
        return None