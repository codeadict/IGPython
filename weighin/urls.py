from django.conf.urls import patterns, url, include
from weighin.views import WeighView

urlpatterns = patterns('',
    url(r'^$', WeighView.as_view(), name="weigh_screen"),
)

