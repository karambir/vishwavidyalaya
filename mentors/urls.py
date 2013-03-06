from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from mentors.views import *

urlpatterns = patterns('',
    url(r'^$', login_required(MenteeRecordsListView.as_view()), name='mentee_list'),
    url(r'^meetings/$', login_required(MenteeMeetingListView.as_view()), name='mentee_meeting_list'),
    url(r'^meetings/(?P<pk>\d+)/$', login_required(MenteeMeetingDetailView.as_view()), name='mentee_meeting_list'),
    url(r'^new-meeting/$', login_required(MenteeMeetingCreateView.as_view()), name='new_mentors_meeting'),
)
