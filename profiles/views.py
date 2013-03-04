from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, CreateView, DetailView

from django.contrib.auth.models import User
from profiles.models import Faculty, Student


class FacultyListView(ListView):
    context_object_name = 'faculty_list'
    template_name = 'faculty_list.html'
    model = Faculty

class FacultyDetailView(DetailView):
    context_object_name = 'faculty'
    template_name = 'faculty_detail.html'
    model = Faculty

class FacultyCreateView(CreateView):
    model = Faculty
    template_name = 'faculty_create.html'
    success_url = '/'

