# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from hauliers.models import Haulier
from hauliers import forms

from django.utils.translation import ugettext as _
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
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

class HaulierCreate(FormView):
    """
    Class to Edit hauliers
    """
    form_class = forms.CreateHaulier
    template_name="hauliers/create.html"
    success_url = '/hauliers/'


    def dispatch(self, request, *args, **kwargs):
        return super(HaulierCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newhaulier = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error creating this Haulier. %s") % e)

        return super(HaulierCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['create_form'] = kwargs.pop('form', None)
        return super(HaulierCreate, self).get_context_data(**kwargs)

    def get_success_url(self):
        messages.success(self.request, _(u"New haulier created."))
        return reverse('haulier_list')
