from django.conf.urls import patterns, include, url
from base.views import edit_settings, UsersList, DeviceList, base_data


urlpatterns = patterns('',
    url(r'^config/$', edit_settings, name="configure"),
    url(r'^config/operators/$', UsersList.as_view(), name="configure_operators"),
    url(r'^config/devices/$', DeviceList.as_view(), name="configure_devices"),
    url(r'^config/basedata/$', base_data, name="configure_data"),
)