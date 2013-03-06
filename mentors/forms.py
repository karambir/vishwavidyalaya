from django import forms
from django.forms import ModelForm
from mentors.models import Mentee

class MenteeUpdateForm(ModelForm):
    class Meta:
        model = Mentee
        exclude = ('student',)
