from django.conf.urls import patterns, include, url
from sources.views import SourcesList
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = patterns('',
    #List view
    url(r'^$', login_required(SourcesList.as_view()), name='sources_list'),
)