from django.db import models
from profiles.models import Faculty
from school.models import Section, Subject, Session

from django.core.urlresolvers import reverse


class News(models.Model):
    faculty = models.ForeignKey(Faculty)
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    class Meta():
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.id})

CLASS_TYPE = ('Lecture', 'Tutorial', 'Lab', 'Free')

class FacultyTimeTable(models.Model):
    faculty = models.ForeignKey(Faculty)
    class_type = models.CharField(max_length='20', choices=zip(CLASS_TYPE,CLASS_TYPE))
    section = models.ForeignKey(Section, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True)
    weekday = models.CharField(max_length=12)
    number = models.IntegerField()
    session = models.ForeignKey(Session)

