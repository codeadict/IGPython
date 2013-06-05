from django.conf.urls import patterns, include, url
from vehicles.views import VehiclesList
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', VehiclesList.as_view(), name='vehicle_list'),
)
