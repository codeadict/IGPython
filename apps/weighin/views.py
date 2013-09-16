from django.views import generic
from django.utils.translation import gettext as _

from transactions.forms import TransactionForm


class WeighView(generic.TemplateView):
    template_name="weighin/main.html"

    def dispatch(self, request, *args, **kwargs):
        return super(WeighView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(WeighView, self).get_context_data(**kwargs)
        form = TransactionForm
        ctx['form'] = form
        ctx['title'] = _('New Transaction')
        return ctx