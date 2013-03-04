from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from mentors.views import MenteeRecordsListView, MenteeMeetingCreateView, MenteeMeetingListView

urlpatterns = patterns('',
    url(r'^$', login_required(MenteeRecordsListView.as_view()), name='mentors_home'),
    url(r'^meetings/$', login_required(MenteeMeetingListView.as_view()), name='mentee_meeting_list'),
    url(r'^new-meeting/$', login_required(MenteeMeetingCreateView.as_view()), name='mentors_meeting'),
)
