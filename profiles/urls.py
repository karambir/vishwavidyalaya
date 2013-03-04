from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from profiles.views import *

urlpatterns = patterns('',
    url(r'^faculty/$', login_required(FacultyListView.as_view()), name='faculty_list'),
    url(r'^faculty/(?P<pk>\d+)/$', login_required(FacultyDetailView.as_view()), name='faculty_detail'),
    url(r'^faculty/new/$', login_required(FacultyCreateView.as_view()), name='faculty_create'),
    url(r'^student/(?P<pk>\d+)/$', login_required(StudentDetailView.as_view()), name='student_detail'),
    url(r'^student/new/$', login_required(StudentCreateView.as_view()), name='student_create'),
)
