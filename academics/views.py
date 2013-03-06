from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, UpdateView
from django.forms.models import modelformset_factory
from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User
from profiles.models import Faculty, Student
from academics.models import Performance, Subject

from academics.forms import *

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


