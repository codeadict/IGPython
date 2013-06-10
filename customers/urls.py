from django.conf.urls import patterns, include, url
from customers.views import CustomersList, CustomerView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(CustomersList.as_view()), name='customer_list'),
    url('^(?P<pk>\d+)/$', CustomerView.as_view(), name='customer_details'),
)