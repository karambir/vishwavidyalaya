from django.db import models
from django.contrib.auth.models import User
from school.models import Course, Section, Subject, School, Department

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)


class Director(models.Model):
    empID = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('director_detail', kwargs={'pk': self.id})


class Faculty(models.Model):
    empID = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    designation = models.CharField(max_length=50)
    qualification = models.CharField(max_length=300, blank=True, null=True)
    experience = models.PositiveIntegerField(default=0, help_text='in years')
    school = models.ForeignKey(School)
    department = models.ForeignKey(Department)
    phone = models.BigIntegerField(null=True, blank=True)
    alternate_phone = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, default='')
    address_street = models.CharField(max_length=350, blank=True, null=True)
    address_city = models.CharField(max_length=100, null=True, blank=True)
    address_state = models.CharField(max_length=30, null=True, blank=True)
    address_pincode = models.IntegerField(null=True, blank=True)
    #is_mentor = models.BooleanField(default=False)
    #is_coordinator = models.BooleanField(default=False)
    #is_hod = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __unicode__(self):
        return '%s %s' %(self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('faculty_detail', kwargs={'pk': self.id})

    def is_hod(self):
        if self.department.hod == self:
            return True
        else:
            return False

    def is_coordinator(self):
        school_courses = Course.objects.filter(department = self.department)
        for course in school_courses:
            if course.coordinator == self:
                return True
        return False

GROUP_CHOICES = (
        (1, 1),
        (2, 2),
)

class Student(models.Model):
    enrollment_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    exam_roll = models.CharField(max_length=20, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    email = models.EmailField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    school = models.ForeignKey(School)
    course = models.ForeignKey(Course)
    section = models.ForeignKey(Section, null=True, blank=True)
    group = models.IntegerField(max_length=1, choices=GROUP_CHOICES, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)

    class Meta:
        permissions = (
                ('view_student', 'Can View Student Profile'),
                )

    def __unicode__(self):
        if self.last_name:
            return '%s %s' %(self.first_name, self.last_name)
        else:
            return self.first_name

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.id})

    def get_full_name(self):
        return self.first_name+' '+self.last_name
