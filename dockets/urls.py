from django.conf.urls import patterns, include, url
from dockets.views import DocketList
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(DocketList.as_view()), name='docket_list'),
)