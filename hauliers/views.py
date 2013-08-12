# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from hauliers.models import Haulier
from hauliers import forms

from django.utils.translation import ugettext as _
from django.views.generic.list import ListView
from django.views import generic
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib import messages

class HauliersList(ListView):
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
