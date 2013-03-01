from django.db import models
from profiles.models import Faculty
from academics.models import Section

GROUP_CHOICES = (
        (1, 1),
        (2, 2),
)

class Mentor(models.Model):
    faculty = models.ForeignKey(Faculty)
    section = models.ForeignKey(Section)
    group = models.IntegerField(max_length=1, choices=GROUP_CHOICES)

    def __unicode__(self):
        return '%s - %s - %s' %(self.faculty, self.section, self.group)
