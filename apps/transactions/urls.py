from django.conf.urls import patterns, include, url
from transactions.views import NewTransaction
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url('^new/$', login_required(NewTransaction.as_view()), name='new_transaction'),
)