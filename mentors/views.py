from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, CreateView, DetailView

from django.contrib.auth.models import User
from profiles.models import Faculty, Student
from mentors.models import MenteeMeeting, Mentee

class MenteeDetailView(DetailView):
    context_object_name = 'mentee'
    template_name = 'mentee_detail.html'
    model = Mentee


class MenteeListView(ListView):
    context_object_name = 'mentee_list'
    template_name = 'mentee_list.html'
    model = Mentee

class MenteeMeetingListView(ListView):
    context_object_name = 'meeting_list'
    template_name = 'meeting_list.html'
    model = MenteeMeeting


class MenteeMeetingDetailView(DetailView):
    model = MenteeMeeting
    context_object_name = 'meeting'
    template_name = 'meeting_detail.html'

class MenteeMeetingCreateView(CreateView):
    model = MenteeMeeting
    template_name = 'mentee_meeting_create.html'
    success_url = '/mentee/meetings/'

