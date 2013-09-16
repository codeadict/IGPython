# -*- coding: utf-8 -*-
from vehicles.models import Vehicles
from vehicles import forms

from django.utils.translation import ugettext as _
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext

from django.core.urlresolvers import reverse

from django.contrib import messages

class VehiclesList(generic.ListView):
    """
    Class to list vehicles
    """
    context_object_name = "vehicle_list"
    queryset = Vehicles.objects.all()
    template_name = "vehicles/list_view.html"

class VehicleView(generic.DetailView):
    model = Vehicles
    context_object_name='vehicle'
    template_name="vehicles/view.html"
    
    
class VehicleCreate(generic.CreateView):
    """
    Class to Edit vehicles
    """    
    form_class = forms.CreateVehicle
    model = Vehicles
    template_name="vehicles/create.html"
    
    def dispatch(self, request, *args, **kwargs):   
        return super(VehicleCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newvehicle = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error creating this Vehicle. %s") % e)

        return super(VehicleCreate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super(VehicleCreate, self).get_context_data(**kwargs)
        ctx['title'] = _("Create vehicle")
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"New vehicle created."))
        return reverse('vehicle_list')

class VehicleUpdate(generic.UpdateView):
    template_name = 'vehicles/create.html'
    model = Vehicles
    form_class = forms.CreateVehicle

    def get_context_data(self, **kwargs):
        ctx = super(VehicleUpdate, self).get_context_data(**kwargs)
        ctx['title'] = _("Update vehicle with driver '%s'") % self.object.driver_name
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Vehicle updated successfully"))
        return reverse('vehicle_list')
    
def delete_vehicle(request, vehicle_id):
    """
    Deletes a Source
    """
    object = get_object_or_404(Vehicles, pk=vehicle_id)
    delete_url = reverse('vehicle_delete', kwargs={'vehicle_id': vehicle_id})
    object_name = 'Vehicle'

    if request.method == 'GET':
        # Render the confirmation page
        return render_to_response('includes/delete_view.html', {
            'object': object, 'delete_url': delete_url, 'object_name': object_name}, context_instance=RequestContext(request))

    # Handle confirm delete form POST
    object.delete()

    return HttpResponseRedirect(reverse('vehicle_list'))

    
    


    
    

