from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, UpdateView
from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from profiles.models import Faculty, Student, Director
from academics.models import Performance, FacultyAssign

from academics.forms import *

def performance_home(request, assign=None):
    director = False
    try:
        u = Director.objects.get(user=request.user)
        director = True
    except:
        u = Faculty.objects.get(user=request.user)
    if director:
        return render_to_repsonse('performance_denied.html', context_instance=RequestContext(request))
    try:
        faculty_assigns = FacultyAssign.objects.filter(faculty=u) #TODO add session filter
        if assign:
            section_to_show = faculty_assigns.get(id=assign)
        else:
            section_to_show = faculty_assigns[0]
        performances = Performance.objects.filter(student__in=Student.objects.filter(section=section_to_show.section)).filter(subject=faculty_assigns[0].subject) #TODO add session
    except:
        faculty_assigns = None
        performances = None
        section_to_show = None
    return render_to_response('performance_section_view.html', {'section_to_show': section_to_show, 'faculty_assigns': faculty_assigns, 'performances': performances}, context_instance=RequestContext(request))

class PerformanceListView(ListView):
    context_object_name = 'performance_list'
    template_name = 'performance_list.html'
    model = Performance

class PerformanceUpdateView(UpdateView):
    model = Performance
    form_class = PerformanceUpdateForm
    template_name = 'performance_update.html'
    success_url = '/academics/performance/'

    def get_context_data(self, **kwargs):
        context = super(PerformanceUpdateView, self).get_context_data(**kwargs)
        context['student'] = Performance.objects.get(id=self.kwargs['pk']).student
        return context

def performance_inline(request):
    PerformanceFormSet = inlineformset_factory(Subject, Performance, extra=0, can_delete=False)
    subject = Subject.objects.get(id=3)
    if request.method == 'POST':
        formset = PerformanceFormSet(request.POST, instance=subject)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/academics/performance/')
    else:
        formset = PerformanceFormSet(instance=subject)
    return render_to_response('performance_inline_update.html', {'formset':formset,}, context_instance=RequestContext(request))


