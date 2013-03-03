from django.db import models
from profiles.models import Faculty, Student
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

class MenteeMeeting(models.Model):
    mentor = models.ForeignKey(Mentor)
    student = models.ForeignKey(Student)
    date = models.DateField()
    remarks = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s - %s on %s' %(self.mentor.faculty.user.first_name, self.student.first_name, self.date)
