from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from academics.views import *

urlpatterns = patterns('',
    url(r'^performance/$', performance_home, name='performance_home'),
    url(r'^performance/(?P<assign>\d+)/$', performance_home, name='performance_section'),
    #url(r'^performance/$', PerformanceListView.as_view(), name='performance_section'),
    #url(r'^student/(?P<pk>\d+)/$', PerformanceUpdateView.as_view(), name='performance_update'),
    #url(r'^performance/edit/$', performance_inline),
)
