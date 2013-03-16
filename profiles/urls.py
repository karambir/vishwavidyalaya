from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from profiles.views import *

urlpatterns = patterns('',
    url(r'^director/$', login_required(DirectorListView.as_view()), name='director_list'),
    url(r'^director/(?P<pk>\d+)/$', login_required(DirectorDetailView.as_view()), name='director_detail'),
    url(r'^faculty/$', login_required(FacultyListView.as_view()), name='faculty_list'),
    url(r'^faculty/(?P<pk>\d+)/$', login_required(FacultyDetailView.as_view()), name='faculty_detail'),
    url(r'^faculty/new/$', login_required(FacultyCreateView.as_view()), name='faculty_create'),
    url(r'^student/$', login_required(StudentListView.as_view()), name='student_list'),
    url(r'^student/(?P<pk>\d+)/$', login_required(StudentDetailView.as_view()), name='student_detail'),
    url(r'^student/(?P<pk>\d+)/edit/$', login_required(StudentUpdateView.as_view()), name='student_update'),
    url(r'^student/new/$', login_required(StudentCreateView.as_view()), name='student_create'),
)
