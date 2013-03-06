from django.db import models
from academics.models import Section, Subject
from profiles.models import Faculty

CLASS_TYPES = (
        ('Free', 'Free'),
        ('Lecture', 'Lecture'),
        ('Tutorial', 'Tutorial'),
        ('Lab', 'Lab'),
)

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

class TimeTable(models.Model):
    faculty = models.ForeignKey(Faculty)
    class_type = models.CharField(max_length=20, choices=CLASS_TYPES, default='Free')
    section = models.ForeignKey(Section, blank=True, null=True)
    weekday = models.CharField(max_length=10, choices=zip(WEEKDAYS, WEEKDAYS), default='Monday')
    number = models.IntegerField(choices=zip(range(1,8), range(1,8)))
    subject = models.ForeignKey(Subject, null=True, blank=True)

    def __unicode__(self):
        return '%s -- %s %d - %s' %(self.faculty, self.weekday, self.number, self.subject)
