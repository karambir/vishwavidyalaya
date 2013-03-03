from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from mentors.views import MenteeRecordsListView

urlpatterns = patterns('',
    url(r'^$', login_required(MenteeRecordsListView.as_view()), name='mentors_home'),
)
