# -*- coding: utf-8 -*-
from dockets.models import Docket

from django.views.generic.list import ListView

from django.contrib import messages


class DocketList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "docket_list"
    queryset = Docket.objects.all()
    template_name = "dockets/list_view.html"
