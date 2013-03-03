from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView

from django.contrib.auth.models import User
from profiles.models import Faculty, Student
from academics.models import Performance

class AttendanceListView(ListView):
    context_object_name = 'attendance_list'
    template_name = 'attendance_list.html'
    model = Performance

class MarksListView(ListView):
    context_object_name = 'marks_list'
    template_name = 'marks_list.html'
    model = Performance
