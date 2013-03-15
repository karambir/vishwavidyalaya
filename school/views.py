from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import UpdateView, CreateView, DetailView, ListView

from school.models import School, Course, Department, Section, Subject
from profiles.models import Student, Faculty, Director

def school_overview(request):
    hod = False
    director = False
    try:
        u = Director.objects.get(user=request.user)
        director = True
    except:
        u = Faculty.objects.get(user=request.user)
        hod = u.is_hod()
    school = u.school
    return render_to_response('school_overview.html', {'school':school, 'hod': hod}, context_instance=RequestContext(request))


class DeptListView(ListView):
    context_object_name = 'departments'
    template_name = 'dept_list.html'

    def get_queryset(self):
        logged_user = self.request.user
        try:
            u = Director.objects.get(user=logged_user)
        except:
            u = Faculty.objects.get(user=logged_user)
        user_school = u.school
        return Department.objects.filter(school=user_school)

    def get_context_data(self, **kwargs):
        context = super(DeptListView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        try:
            u = Director.objects.get(user=logged_user)
        except:
            u = Faculty.objects.get(user=logged_user)
        user_school = u.school
        context['school'] = user_school
        return context


class CourseListView(ListView):
    context_object_name = 'courses'
    template_name = 'course_list.html'

    def get_queryset(self):
        logged_user = self.request.user
        try:
            u = Director.objects.get(user=logged_user)
        except:
            u = Faculty.objects.get(user=logged_user)
        user_school = u.school
        return Course.objects.filter(school=user_school)

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        try:
            u = Director.objects.get(user=logged_user)
        except:
            u = Faculty.objects.get(user=logged_user)
        user_school = u.school
        context['school'] = user_school
        return context


class SectionListView(ListView):
    context_object_name = 'sections'
    template_name = 'section_list.html'

    def get_queryset(self):
        logged_user = self.request.user
        try:
            u = Director.objects.get(user=logged_user)
        except:
            u = Faculty.objects.get(user=logged_user)
        user_school = u.school
        return Section.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        logged_user = self.request.user
        try:
            u = Director.objects.get(user=logged_user)
        except:
            u = Faculty.objects.get(user=logged_user)
        user_school = u.school
        context['school'] = user_school
        return context


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

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = Course.objects.get(id=self.kwargs['pk'])
        sections = course.section_set.all()
        context['sections'] = sections
        return context


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

    def get_context_data(self, **kwargs):
        context = super(SectionDetailView, self).get_context_data(**kwargs)
        sec = Section.objects.get(id=self.kwargs['pk'])
        students = sec.student_set.all()
        context['students'] = students
        return context


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
    context_object_name = 'department'
    template_name = 'dept_detail.html'
    model = Department

    def get_context_data(self, **kwargs):
        context = super(DeptDetailView, self).get_context_data(**kwargs)
        dept = Department.objects.get(id=self.kwargs['pk'])
        courses = dept.course_set.all()
        context['courses'] = courses
        return context


class DeptCreateView(CreateView):
    model = Department
    template_name = 'dept_create.html'

class DeptUpdateView(UpdateView):
    model = Department
    template_name = 'dept_update.html'

