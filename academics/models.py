from django.db import models
#from profiles.models import Faculty, Student


class Course(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    batch = models.IntegerField()

    def __unicode__(self):
        return self.name

SUBJECT_STATUS = (
        ('Compulsory', 'Compulsory'),
        ('Optional', 'Optional'),
)

class Teach(models.Model):
    faculty = models.ForeignKey('profiles.Faculty')
    section = models.ForeignKey(Section)
    subject = models.ForeignKey(Subject)
    status = models.CharField(max_length = 15, choices = SUBJECT_STATUS)

    def __unicode__(self):
        return '%s teaches %s to %s class' %(self.faculty, self.subject, self.section)

class Performance(models.Model):
    student = models.ForeignKey('profiles.Student')
    subject = models.ForeignKey(Subject)
    sessional1 = models.IntegerField(default=0)
    sessional2 = models.IntegerField(default=0)
    quiz = models.IntegerField(default=0)
    attendance = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return '%s %s' %(self.student, self.subject)

