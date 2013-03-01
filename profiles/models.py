from django.db import models
from django.contrib.auth.models import User
from academics.models import Course, Section

SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)

class Faculty(models.Model):
    empID = models.IntegerField(unique=True)
    user = models.ForeignKey(User)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone = models.BigIntegerField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user.first_name)

GROUP_CHOICES = (
        (1, 1),
        (2, 2),
)

class Student(models.Model):
    enrolment_number = models.CharField(max_length=15)
    form_number = models.IntegerField(null=True, blank=True)
    exam_roll = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    course = models.ForeignKey(Course)
    section = models.ForeignKey(Section)
    group = models.IntegerField(max_length=1, choices=GROUP_CHOICES, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)
