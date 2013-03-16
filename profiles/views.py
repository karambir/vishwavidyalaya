from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from django.contrib.auth.models import User
from profiles.models import Faculty, Student, Director

class DirectorListView(ListView):
    context_object_name = 'directors'
    template_name = 'director_list.html'
    model = Director

class DirectorDetailView(DetailView):
    context_object_name = 'director'
    template_name = 'director_detail.html'
    model = Director

class FacultyListView(ListView):
    context_object_name = 'faculties'
    template_name = 'faculty_list.html'
    model = Faculty

class FacultyDetailView(DetailView):
    context_object_name = 'faculty'
    template_name = 'faculty_detail.html'
    model = Faculty

class FacultyCreateView(CreateView):
    model = Faculty
    template_name = 'faculty_create.html'

class StudentListView(ListView):
    context_object_name = 'students'
    template_name = 'student_list.html'
    model = Student

class StudentDetailView(DetailView):
    context_object_name = 'student'
    template_name = 'student_detail.html'
    model = Student

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_create.html'

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_update.html'
