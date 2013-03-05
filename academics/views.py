from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, UpdateView

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

class PerformanceUpdateView(UpdateView):
    model = Performance
    template_name = 'performance_update.html'
    success_url = '/academics/marks/'


