from django.db import models
#from profiles.models import Faculty, Student
from school.models import Section, Subject, Session

class FacultyAssign(models.Model):
    faculty = models.ForeignKey('profiles.Faculty')
    section = models.ForeignKey(Section)
    subject = models.ForeignKey(Subject)
    session = models.ForeignKey(Session)

    class Meta:
        permissions = (
                ('view_facultyassign', 'Can view Faculty Assigned'),
                )

    def __unicode__(self):
        return '%s %s %s' %(self.faculty, self.section, self.subject)

class Performance(models.Model):
    student = models.ForeignKey('profiles.Student')
    subject = models.ForeignKey(Subject)
    session = models.ForeignKey(Session)
    sessional1 = models.IntegerField(null=True, blank=True, default=0)
    sessional2 = models.IntegerField(null=True, blank=True, default=0)
    quiz = models.IntegerField(null=True, blank=True, default=0)
    attendance = models.IntegerField(null=True, blank=True, default=0)
    total_attendance = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        permissions = (
                ('view_performance', 'Can view Performance'),
                )

    def get_attendance(self):
        return round((int(self.attendance)*100)/float(self.total_attendance), 2)

    def __unicode__(self):
        return '%s %s' %(self.student, self.subject)

