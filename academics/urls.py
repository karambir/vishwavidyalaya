from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from academics.views import AttendanceListView, MarksListView

urlpatterns = patterns('',
    url(r'^attendance/$', login_required(AttendanceListView.as_view()), name='attendance_home'),
    url(r'^marks/$', login_required(MarksListView.as_view()), name='marks_home'),
)
