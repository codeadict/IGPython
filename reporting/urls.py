from django.conf.urls import patterns, include, url
from reporting.views import IndexView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(IndexView.as_view()), name='dasboard'),
)