from django.conf.urls import patterns, include, url
from vehicles.views import VehiclesList, VehicleCreate, VehicleView, VehicleUpdate
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', VehiclesList.as_view(), name='vehicle_list'),
    url('^create/$', VehicleCreate.as_view(), name='vehicle_create'),
    url('^(?P<pk>\d+)/$', VehicleView.as_view(), name='vehicle_details'),
    url(r'^(?P<pk>\d+)/update/$', VehicleUpdate.as_view(), name='vehicle_update'),
)
