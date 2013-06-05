from vehicles.models import Vehicles
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect

from django.contrib import messages

class VehiclesList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "vehicle_list"
    queryset = Vehicles.objects.all()
    template_name = "vehicles/list_view.html"
    
    

