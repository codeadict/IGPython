# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from datetime import timedelta
from decimal import Decimal as D, ROUND_UP

from django.utils.translation import gettext as _
#from django.utils.timezone import now
from datetime import date 
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.http import Http404
from django.db.models import Avg, Sum, Count
from django.contrib import messages

from dockets.models import Docket
from hauliers.models import Haulier
from vehicles.models import Vehicles
from customers.models import Customer

from reporting.forms import ReportForm
from reporting.utils import ReportList

class IndexView(TemplateView):
    """
    Dashboard Reporting
    """
    template_name = 'model_report/report_list.html'
    report_form_class = ReportForm
    generator_repository = ReportList

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx.update(self.get_stats())
        ctx['form'] = self.report_form_class()
        return ctx

    def _get_generator(self, form):
        code = form.cleaned_data['report_type']

        repo = self.generator_repository()
        generator_cls = repo.get_generator(code)
        if not generator_cls:
            raise Http404()

        formatter = form.cleaned_data['report_format']

        return generator_cls(formatter=formatter)

    def get(self, request, *args, **kwargs):
        if 'report_type' in request.GET:
            form = self.report_form_class(request.GET)
            if form.is_valid():
                generator = self._get_generator(form)
                report = generator.generate()
                return report
            else:
                messages.error(self.request, _('You must fill all the fields'))
        return TemplateResponse(request, self.template_name, self.get_context_data())

    def tickets_per_week_report(self, segments=5):
        # Get datetime for 24 hours agao
        time_now = date.today()
        gt_time = time_now - timedelta(days=7)

        tickets_last_week = Docket.objects.filter(docket_date__gt=gt_time)
        tickets_total_daily = []
        for day in range(0, 7, 1):
            lt_time = gt_time + timedelta(days=1)
            daily_orders = tickets_last_week.filter(docket_date__gte=gt_time, docket_date__lte=lt_time)
            print daily_orders
            total = daily_orders.count() or 0
            tickets_total_daily.append({
                'day': lt_time,
                'total': D(total)
            })

            gt_time = lt_time

        max_value = max([x['total'] for x in tickets_total_daily])
        print max_value
        divisor = 1
        while divisor < max_value / 50:
            divisor *= 10
        max_value = (max_value / divisor).quantize(D('1'), rounding=ROUND_UP)
        max_value *= divisor
        if max_value:
            segment_size = (max_value) / D('100.0')
            for item in tickets_total_daily:
                item['percentage'] = int(item['total'] / segment_size)

            y_range = []
            y_axis_steps = max_value / D(str(segments))
            for idx in reversed(range(segments+1)):
                y_range.append(idx * y_axis_steps)
        else:
            y_range = []
            for item in tickets_total_daily:
                item['percentage'] = 0

        ctx = {
            'tickets_total_daily': tickets_total_daily,
            'max_value': max_value,
            'y_range': y_range,
        }
        return ctx

    def get_stats(self):
        """
        Get some Statistics
        """
        datetime_24hrs_ago = date.today() - timedelta(hours=24)

        tickets = Docket.objects.filter()
        tickets_last_day = tickets.filter(docket_date__gt=datetime_24hrs_ago)

        #stats dict
        stats = {
            'total_tickets_last_day': tickets_last_day.count(),
            'active_hauliers': Haulier.objects.filter(active=True).count(),
            'active_vehicles': Vehicles.objects.filter(active=True).count(),
            'active_customers': Customer.objects.filter(active=True).count(),
            'weekly_report_dict': self.tickets_per_week_report()
        }

        return stats