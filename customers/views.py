# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from customers.models import Customer
from customers import forms

from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import generic

from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateResponseMixin
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib import messages

class CustomersList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "customer_list"
    queryset = Customer.objects.all()
    template_name = "customers/list_view.html"

class CustomerView(DetailView):
    model = Customer
    context_object_name='customer'
    template_name="customers/view.html"

class CustomerCreate(generic.CreateView):
    """
    Class to Edit vehicles
    """
    form_class = forms.CreateCustomer
    template_name="customers/create.html"
    model = Customer


    def dispatch(self, request, *args, **kwargs):
        return super(CustomerCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newcustomer = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error creating this Customer. %s") % e)

        return super(CustomerCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CustomerCreate, self).get_context_data(**kwargs)
        ctx['title'] = _("Create customer ")
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"New customer created."))
        return reverse('customer_list')

class CustomerUpdate(generic.UpdateView):
    """
    Class to Edit vehicles
    """
    form_class = forms.CreateCustomer
    template_name="customers/create.html"
    model = Customer

    def get_context_data(self, **kwargs):
        ctx = super(CustomerUpdate, self).get_context_data(**kwargs)
        ctx['title'] = _("Edit customer '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"New customer created."))
        return reverse('customer_list')