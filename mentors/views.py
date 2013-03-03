from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView

from django.contrib.auth.models import User
from profiles.models import Faculty, Student

class MenteeRecordsListView(ListView):
    context_object_name = 'mentee_list'
    template_name = 'mentee_record_list.html'
    model = Student

