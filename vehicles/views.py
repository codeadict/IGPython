# -*- coding: utf-8 -*-

from vehicles.models import Vehicles
from vehicles import forms

from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateResponseMixin

from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404

from django.contrib import messages
from django.db import transaction

class VehiclesList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "vehicle_list"
    queryset = Vehicles.objects.all()
    template_name = "vehicles/list_view.html"
    
    
class VehicleView(DetailView):
    model = Vehicles
    context_object_name='vehicle'
    template_name="vehicles/view.html"
    
    
class VehicleCreate(FormView, TemplateResponseMixin):
    """
    Class to Edit vehicles
    """    
    form_class = forms.CreateVehicle
    template_name="vehicles/create.html"
    success_url = '/vehicles/'
    
    def dispatch(self, request, *args, **kwargs):   
        return super(VehicleCreate, self).dispatch(request, *args, **kwargs)
    
    def get_form(self, form_class):
        """
        Returns an instance of the form to be used in this view.
        """
        kwargs = self.get_form_kwargs()
        initial = kwargs.get('initial', {})
        kwargs['initial'] = initial
        form = form_class(self.request, **kwargs)
        form.fields['max_gross'].widget = forms.TextInputAppend(prepend=' T')   
        return form
    
    @transaction.commit_manually
    def form_valid(self, form):
        try:
            self.newvehicle = Vehicles(
                    driver_name = form.cleaned_data['driver_name'],
                    max_gross = form.cleaned_data['max_gross'],
                    use_stored_tare = form.cleaned_data['use_stored_tare'],
                    print_ticket = form.cleaned_data['print_ticket'],
                    reference_number = form.cleaned_data['reference_number'],
                    active = form.cleaned_data['active']
            )
            self.newvehicle.save()
            
            messages.success(self.request, _(u"New vehicle created."))
            transaction.commit()
            
        except Exception, e:
            transaction.rollback()
            messages.error(self.request, _(u"There was an error creating this Vehicle. %s") % e)
            transaction.commit()
        
        transaction.commit()
        return super(VehicleCreate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        kwargs['create_form'] = kwargs.pop('form', None)
        return super(VehicleCreate, self).get_context_data(**kwargs)
    
    
    


    
    

