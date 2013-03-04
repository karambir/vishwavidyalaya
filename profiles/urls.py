from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', login_required(FacultyListView.as_view()), name='faculty_list'),
    url(r'^(?P<pk>\d+)/$', login_required(FacultyDetailView.as_view()), name='faculty_detail'),
    url(r'^new/$', login_required(FacultyCreateView.as_view()), name='faculty_create'),
)
