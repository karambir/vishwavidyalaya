from django.db import models

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
