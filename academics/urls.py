from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from academics.views import *

urlpatterns = patterns('',
    url(r'^performance/$', login_required(PerformanceListView.as_view()), name='attendance_home'),
    url(r'^student/(?P<pk>\d+)/$', login_required(PerformanceUpdateView.as_view()), name='performance_update'),
    url(r'^performance/edit/$', performance_inline),
)
