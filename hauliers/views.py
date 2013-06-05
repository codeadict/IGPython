from hauliers.models import Haulier
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect

from django.contrib import messages

class HauliersList(ListView):
    """
    Class to list Hauliers
    """
    context_object_name = "haulier_list"
    queryset = Haulier.objects.all()
    template_name = "hauliers/list_view.html"
