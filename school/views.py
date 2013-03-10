from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import UpdateView, CreateView, DetailView

from school.models import School, Course, Department, Section, Subject
from profiles.models import Student, Faculty, Director

def school_overview(request):
    try:
        u = Director.objects.get(user=request.user)
    except:
        u = Faculty.objects.get(user=request.user)
    school = u.school
    return render_to_response('school_overview.html', {'school':school}, context_instance=RequestContext(request))


class SchoolDetailView(DetailView):
    context_object_name = 'school'
    template_name = 'school_detail.html'
    model = School

class SchoolCreateView(CreateView):
    model = School
    template_name = 'school_create.html'

class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school_update.html'

class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'course_detail.html'
    model = Course

class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_create.html'

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'course_update.html'

class SectionDetailView(DetailView):
    context_object_name = 'section'
    template_name = 'section_detail.html'
    model = Section

class SectionCreateView(CreateView):
    model = Section
    template_name = 'section_create.html'

class SectionUpdateView(UpdateView):
    model = Section
    template_name = 'section_update.html'

class SubjectDetailView(DetailView):
    context_object_name = 'subject'
    template_name = 'subject_detail.html'
    model = Subject

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subject_create.html'

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subject_update.html'

class DeptDetailView(DetailView):
    context_object_name = 'dept'
    template_name = 'dept_detail.html'
    model = Department

class DeptCreateView(CreateView):
    model = Department
    template_name = 'dept_create.html'

class DeptUpdateView(UpdateView):
    model = Department
    template_name = 'dept_update.html'

