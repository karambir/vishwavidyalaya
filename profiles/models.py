from django.db import models
from django.contrib.auth.models import User
from academics.models import Course, Section, Subject, Teach

from django.core.urlresolvers import reverse

SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Teach)
def add_subjects(sender, instance, created, **kwargs):
    if instance.status == 'Compulsory':
        class_students = Student.objects.filter(section= instance.section)
        for stu in class_students:
            instance.subject.student_set.add(stu)

MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
)

class Address(models.Model):
    street = models.CharField(max_length=350, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s - %s - %s' %(self.street, self.city, self.state)

class Faculty(models.Model):
    empID = models.IntegerField(unique=True)
    user = models.ForeignKey(User)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    designation = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    qualification = models.CharField(max_length=300, blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    school = models.CharField(max_length=300)
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUS)
    phone = models.BigIntegerField(null=True, blank=True)
    alternate_phone = models.BigIntegerField(null=True, blank=True)
    permanent_address = models.ForeignKey(Address, related_name='permanent_address', blank=True, null=True)
    correspondence_address = models.ForeignKey(Address, related_name='correspondence_address', blank=True, null=True)
    description = models.TextField(blank=True, default='')


    def get_absolute_url(self):
        return reverse('faculty_detail', kwargs={'pk': self.id})

    def __unicode__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)

GROUP_CHOICES = (
        (1, 1),
        (2, 2),
)

class Student(models.Model):
    enrolment_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    exam_roll = models.CharField(max_length=20, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    alternate_phone = models.BigIntegerField(null=True, blank=True)
    course = models.ForeignKey(Course)
    section = models.ForeignKey(Section)
    group = models.IntegerField(max_length=1, choices=GROUP_CHOICES, null=True, blank=True)
    address = models.ForeignKey(Address, related_name='student_address', blank=True, null=True)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)

    def __unicode__(self):
        return '%s %s' %(self.first_name, self.last_name)
