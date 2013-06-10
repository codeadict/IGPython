from customers.models import Customer
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.http import Http404, HttpResponseRedirect

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