from customers.models import Customer
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect

from django.contrib import messages

class CustomersList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "customer_list"
    queryset = Customer.objects.all()
    template_name = "customers/list_view.html"
