from sources.models import LoadingPoint
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect

from django.contrib import messages

class SourcesList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "source_list"
    queryset = LoadingPoint.objects.all()
    template_name = "sources/list_view.html"
