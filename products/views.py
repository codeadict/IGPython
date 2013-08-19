# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from products.models import Product
from products import forms
from django.views import generic

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from django.contrib import messages

class ProductList(generic.ListView):
    """
    View to list products
    """
    context_object_name = "product_list"
    queryset = Product.objects.all()
    template_name = "products/list_view.html"

class ProductView(generic.DetailView):
    model = Product
    context_object_name='product'
    template_name="products/view.html"

class ProductCreate(generic.CreateView):
    """
    Class to add Products
    """
    form_class = forms.ProductForm
    template_name="products/create.html"
    model = Product

    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newproduct = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error creating this Product. %s") % e)

        return super(ProductCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['title'] = _("Create product ")
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"New product created."))
        return reverse('product_list')


class ProductUpdate(generic.UpdateView):
    """
    Class to Edit vehicles
    """
    form_class = forms.ProductForm
    template_name="products/create.html"
    model = Product

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['title'] = _("Edit product '%s'") % self.object.name
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"Successfully updated product '%s'.") % self.object.name )
        return reverse('product_list')