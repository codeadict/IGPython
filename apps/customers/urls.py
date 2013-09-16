from django.conf.urls import patterns, include, url
from customers.views import CustomersList, CustomerView, CustomerCreate, CustomerUpdate, delete_customer
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(CustomersList.as_view()), name='customer_list'),
    url('^(?P<pk>\d+)/$', CustomerView.as_view(), name='customer_details'),
    url('^create/$', CustomerCreate.as_view(), name='customer_create'),
    url(r'^(?P<pk>\d+)/update/$', CustomerUpdate.as_view(), name='customer_update'),
    url(r'^(?P<customer_id>\d+)/delete/$', delete_customer, name='customer_delete'),
)