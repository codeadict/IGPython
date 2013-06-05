from django.conf.urls import patterns, include, url
from hauliers.views import HauliersList
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(HauliersList.as_view()), name='haulier_list'),
)