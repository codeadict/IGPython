from django.utils.translation import ugettext as _
from django.views import generic
from django.core.urlresolvers import reverse

from django.contrib import messages

from  transactions.models import Transaction
from transactions import forms as t_forms


class NewTransaction(generic.FormView):
    """
    Class to Edit hauliers
    """
    form_class = t_forms.TransactionForm
    template_name="weighin/transaction_popup.html"


    def dispatch(self, request, *args, **kwargs):
        return super(NewTransaction, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            self.newtransaction = form.save()
        except Exception, e:
            messages.error(self.request, _(u"There was an error on Transaction."))

        return super(NewTransaction, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(NewTransaction, self).get_context_data(**kwargs)
        ctx['title'] = _("New Transaction")
        return ctx

    def get_success_url(self):
        messages.success(self.request, _(u"Transaction Done Successfully."))

