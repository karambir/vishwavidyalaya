from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, CreateView

from django.contrib.auth.models import User
from profiles.models import Faculty, Student
from mentors.models import MenteeMeeting


class MenteeRecordsListView(ListView):
    context_object_name = 'mentee_list'
    template_name = 'mentee_record_list.html'
    model = Student

class MenteeMeetingCreateView(CreateView):
    model = MenteeMeeting
    template_name = 'mentee_meeting_create.html'

