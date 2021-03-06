# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from hauliers.models import Haulier
from hauliers import forms

from django.utils.translation import ugettext as _
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext

from django.core.urlresolvers import reverse

from django.contrib import messages

class HaulierView(generic.DetailView):
    model = Haulier
    context_object_name='haulier'
    template_name="hauliers/view.html"

class HauliersList(generic.ListView):
    """
    Class to list Hauliers
    """
    context_object_name = "haulier_list"
    queryset = Haulier.objects.all()
    template_name = "hauliers/list_view.html"

class HaulierCreate(generic.CreateView):
    """
    Class to Edit hauliers
    """
    form_class = forms.CreateHaulier
    template_name="hauliers/create.html"
    model = Haulier


    def dispatch(self, request, *args, **kwargs):
        return super(HaulierCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newhaulier = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error creating this Haulier. %s") % e)

        return super(HaulierCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(HaulierCreate, self).get_context_data(**kwargs)
        ctx['title'] = _("Create haulier")
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"New haulier created."))
        return reverse('haulier_list')

class HaulierUpdate(generic.UpdateView):
    template_name = 'hauliers/create.html'
    model = Haulier
    form_class = forms.CreateHaulier

    def get_context_data(self, **kwargs):
        ctx = super(HaulierUpdate, self).get_context_data(**kwargs)
        ctx['title'] = _("Update haulier '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Haulier updated successfully"))
        return reverse('haulier_list')

def delete_haulier(request, haulier_id):
    """
    Deletes a Haulier
    """
    object = get_object_or_404(Haulier, pk=haulier_id)
    delete_url = reverse('haulier_delete', kwargs={'haulier_id': haulier_id})
    object_name = 'Haulier'

    if request.method == 'GET':
        # Render the confirmation page
        return render_to_response('includes/delete_view.html', {
            'object': object, 'delete_url': delete_url, 'object_name': object_name}, context_instance=RequestContext(request))

    # Handle confirm delete form POST
    object.delete()

    return HttpResponseRedirect(reverse('haulier_list'))