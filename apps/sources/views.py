# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from sources.models import LoadingPoint
from sources import forms

from django.utils.translation import ugettext as _
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext

from django.core.urlresolvers import reverse

from django.contrib import messages

class SourcesList(generic.ListView):
    """
    Class to list vehicles
    """
    context_object_name = "source_list"
    queryset = LoadingPoint.objects.all()
    template_name = "sources/list_view.html"

class SourcesView(generic.DetailView):
    """
    Detail View
    """
    model = LoadingPoint
    context_object_name = 'source'
    template_name = "sources/view.html"

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

def delete_source(request, source_id):
    """
    Deletes a Source
    """
    object = get_object_or_404(LoadingPoint, pk=source_id)
    delete_url = reverse('source_delete', kwargs={'source_id': source_id})
    object_name = 'Loading Point'

    if request.method == 'GET':
        # Render the confirmation page
        return render_to_response('includes/delete_view.html', {
            'object': object, 'delete_url': delete_url, 'object_name': object_name}, context_instance=RequestContext(request))

    # Handle confirm delete form POST
    object.delete()

    return HttpResponseRedirect(reverse('sources_list'))
