# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from sources.models import LoadingPoint
from sources import forms

from django.utils.translation import ugettext as _
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views import generic
from django.core.urlresolvers import reverse

from django.contrib import messages

class SourcesList(ListView):
    """
    Class to list vehicles
    """
    context_object_name = "source_list"
    queryset = LoadingPoint.objects.all()
    template_name = "sources/list_view.html"


class SourceCreate(generic.CreateView):
    """
    Class to Edit hauliers
    """
    form_class = forms.CreateSource
    model = LoadingPoint
    template_name="sources/create.html"


    def dispatch(self, request, *args, **kwargs):
        return super(SourceCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newhaulier = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error creating this Source. %s") % e)

        return super(SourceCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(SourceCreate, self).get_context_data(**kwargs)
        ctx['title'] = _("Create source")
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"New source created."))
        return reverse('sources_list')

class SourceUpdate(generic.UpdateView):
    template_name = 'sources/create.html'
    model = LoadingPoint
    form_class = forms.CreateSource

    def get_context_data(self, **kwargs):
        ctx = super(SourceUpdate, self).get_context_data(**kwargs)
        ctx['title'] = _("Update source '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Source updated successfully"))
        return reverse('sources_list')

class SourceDelete(generic.DeleteView):
    template_name = 'dashboard/catalogue/product_delete.html'
    model = LoadingPoint
    context_object_name = 'source'

    def get_success_url(self):
        msg =_("Deleted source '%s'") % self.object.name
        messages.success(self.request, msg)
        return reverse('sources_list')

