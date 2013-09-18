from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from django.conf import settings
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Include Model reports
from model_report import report
report.autodiscover()

from tastypie.api import Api
from weighin.api import TransactionResource, VehicleResource, ProductResource

api = Api(api_name='1.0')
api.register(TransactionResource())
api.register(VehicleResource())
api.register(ProductResource())

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^$', TemplateView.as_view(template_name='base/dashboard.html') , name="index"),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/vehicles/'}, name="logout"),
    url(r'^global/', include('base.urls')),
    url(r'^vehicles/', include('vehicles.urls')),
    url(r'^customers/', include('customers.urls')),
    url(r'^hauliers/', include('hauliers.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^sources/', include('sources.urls')),
    url(r'^transactions/', include('transactions.urls')),
    url(r'^weighin/', include('weighin.urls')),
    url(r'^api/', include(api.urls), name='weigh_api'),
    url(r'^dockets/', include('dockets.urls')),
    url(r'^reports/', include('reporting.urls'), name="reports"),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
