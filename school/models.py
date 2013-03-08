from django.db import models
#from profiles.models import Faculty, Student

SCHOOL_CHOICES = ('Engineering', 'Management', 'Law', 'Applied Sciences', 'Medical')

class School(models.Model):
    name = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    school_type = models.CharField(max_length=70, choices=zip(SCHOOL_CHOICES, SCHOOL_CHOICES))

class Course(models.Model):
    name = models.CharField(max_length=90)
    duration = models.IntegerField(help_text='in years')
    code = models.CharField(max_length=10)
    school = models.ForeignKey(School)
    coordinator = models.ForeignKey('profiles.Faculty')

    def __unicode__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    hod = models.ForeignKey('profiles.Faculty', related_name='hod')
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    batch = models.IntegerField()
    school = models.ForeignKey(School)

    def __unicode__(self):
        return self.name

SEM_CHOICES = ('Even', 'Odd')
YEARS = ('2012-2013', '2013-2014', '2014-2015')

class Session(models.Model):
    year = models.CharField(max_length=15, choices=zip(YEARS, YEARS))
    semester = models.CharField(max_length=15, choices=zip(SEM_CHOICES, SEM_CHOICES))

    def __unicode__(self):
        return '%s %s' %(self.year, self.semester)
