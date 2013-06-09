# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from vehicles.models import Vehicles

from model_report.report import reports, ReportAdmin
from model_report.utils import (usd_format, avg_column, sum_column, count_column)


class VehiclesReport(ReportAdmin):
    title = _('Vehicles Report')
    model = Vehicles
    fields = [
        'driver_name',
        'max_gross',
        'use_stored_tare',
    ]
    type = 'report'

reports.register('vehicles-report', VehiclesReport)