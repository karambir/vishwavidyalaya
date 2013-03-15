from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from school.views import *

urlpatterns = patterns('',
    #url(r'^$', school_overview, name='school_overview'),
    url(r'^$', DeptListView.as_view(), name='dept_list'),
    url(r'^courses/$', CourseListView.as_view(), name='course_list'),
    url(r'^sections/$', SectionListView.as_view(), name='section_list'),
    url(r'^dept/(?P<pk>\d+)/$', DeptDetailView.as_view(), name='dept_detail'),
    url(r'^course/(?P<pk>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^section/(?P<pk>\d+)/$', SectionDetailView.as_view(), name='section_detail'),
    url(r'^subject/(?P<pk>\d+)/$', SubjectDetailView.as_view(), name='subject_detail'),
    url(r'^new/$', SchoolCreateView.as_view(), name='school_create'),
    url(r'^dept/new/$', DeptCreateView.as_view(), name='dept_create'),
    url(r'^course/new/$', CourseCreateView.as_view(), name='course_create'),
    url(r'^section/new/$', SectionCreateView.as_view(), name='section_create'),
    url(r'^subject/new/$', SubjectCreateView.as_view(), name='subject_create'),
    url(r'^(?P<pk>\d+)/edit/$', SchoolUpdateView.as_view(), name='school_update'),
    url(r'^dept/(?P<pk>\d+)/edit/$', DeptUpdateView.as_view(), name='dept_update'),
    url(r'^course/(?P<pk>\d+)/edit/$', CourseUpdateView.as_view(), name='course_update'),
    url(r'^section/(?P<pk>\d+)/edit/$', SectionUpdateView.as_view(), name='section_update'),
    url(r'^subject/(?P<pk>\d+)/edit/$', SubjectUpdateView.as_view(), name='subject_update'),
)
