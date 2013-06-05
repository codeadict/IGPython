from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Serve stactic from Media:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^vehicles/', include('vehicles.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^hauliers/', include('hauliers.urls')),
    url(r'^sources/', include('sources.urls')),
    url(r'^weighin/', include('weighin.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
