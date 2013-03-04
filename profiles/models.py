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

class Faculty(models.Model):
    empID = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    designation = models.CharField(max_length=50)
    qualification = models.CharField(max_length=300, blank=True, null=True)
    experience = models.PositiveIntegerField(default=0, help_text='in years')
    school = models.CharField(max_length=300)
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUS)
    phone = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, default='')
    alternate_phone = models.BigIntegerField(null=True, blank=True)
    address_street = models.CharField(max_length=350, blank=True, null=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_state = models.CharField(max_length=30, null=True, blank=True)
    address_pincode = models.IntegerField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)


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
    subjects = models.ManyToManyField(Subject, null=True, blank=True)
    address_street = models.CharField(max_length=350, blank=True, null=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_state = models.CharField(max_length=30, null=True, blank=True)
    address_pincode = models.IntegerField(null=True, blank=True)

    class Meta:
        permissions = (
                ('view_student', 'Can View Student Profile'),
                )

    def __unicode__(self):
        return '%s %s' %(self.first_name, self.last_name)
