from django import forms
from django.forms import ModelForm

from academics.models import Performance

class PerformanceUpdateForm(ModelForm):
    class Meta:
        model = Performance
        exclude = ('student', 'subject')
