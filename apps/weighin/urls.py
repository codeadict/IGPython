from django.conf.urls import patterns, url, include
from weighin.views import WeighView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', login_required(WeighView.as_view()), name="weigh_screen"),
)

