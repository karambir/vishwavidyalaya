from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from news.views import *

urlpatterns = patterns('',
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<pk>\d+)/$', NewsDetailView.as_view(), name='news_detail'),
)
