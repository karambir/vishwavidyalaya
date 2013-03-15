from django.db import models
from profiles.models import Faculty, Student
from school.models import Section, Session

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Student)
def mentee_creation(sender, instance, created, **kwargs):
    mentee = Mentee.objects.get_or_create(student=instance)

GROUP_CHOICES = (
        (1, 1),
        (2, 2),
)

class Mentor(models.Model):
    faculty = models.ForeignKey(Faculty)
    section = models.ForeignKey(Section)
    group = models.IntegerField(max_length=1, choices=GROUP_CHOICES)
    session = models.ForeignKey(Session)

    def __unicode__(self):
        return '%s - %s - %s' %(self.faculty, self.section, self.group)


class Mentee(models.Model):
    student = models.OneToOneField(Student)

    present_address = models.CharField(max_length=350, blank=True, null=True)
    present_address_phone = models.BigIntegerField(blank=True, null=True)
    present_address_email = models.EmailField(blank=True, null=True)

    permanent_address = models.CharField(max_length=350, blank=True, null=True)
    permanent_address_phone = models.BigIntegerField(blank=True, null=True)
    permanent_address_email = models.EmailField(blank=True, null=True)

    local_guardian_name = models.CharField(max_length=120, null=True, blank=True)
    local_guardian_address = models.CharField(max_length=350, null=True, blank=True)
    local_guardian_phone = models.BigIntegerField(blank=True, null=True)
    local_guardian_email = models.EmailField(blank=True, null=True)

    school_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    school_year = models.IntegerField(null=True, blank=True)
    school_division = models.CharField(max_length=20, null=True, blank=True)
    school_remarks = models.CharField(max_length=350, null=True, blank=True)

    inter_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    inter_year = models.IntegerField(null=True, blank=True)
    inter_division = models.CharField(max_length=20, null=True, blank=True)
    inter_remarks = models.CharField(max_length=350, null=True, blank=True)

    degree_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    degree_year = models.IntegerField(null=True, blank=True)
    degree_division = models.CharField(max_length=20, null=True, blank=True)
    degree_remarks = models.CharField(max_length=350, null=True, blank=True)

    others_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    others_year = models.IntegerField(null=True, blank=True)
    others_division = models.CharField(max_length=20, null=True, blank=True)
    others_remarks = models.CharField(max_length=350, null=True, blank=True)

    family1_name = models.CharField(max_length=120, blank=True, null=True)
    family1_relationship = models.CharField(max_length=20, null=True, blank=True, default='Father')
    family1_age = models.IntegerField(blank=True, null=True)
    family1_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)
    family2_name = models.CharField(max_length=120, blank=True, null=True)
    family2_relationship = models.CharField(max_length=20, null=True, blank=True, default='Mother')
    family2_age = models.IntegerField(blank=True, null=True)
    family2_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)
    family3_name = models.CharField(max_length=120, blank=True, null=True)
    family3_relationship = models.CharField(max_length=20, null=True, blank=True, default='Brother')
    family3_age = models.IntegerField(blank=True, null=True)
    family3_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)
    family4_name = models.CharField(max_length=120, blank=True, null=True)
    family4_relationship = models.CharField(max_length=20, null=True, blank=True, default='Brother')
    family4_age = models.IntegerField(blank=True, null=True)
    family4_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)
    family5_name = models.CharField(max_length=120, blank=True, null=True)
    family5_relationship = models.CharField(max_length=20, null=True, blank=True, default='Sister')
    family5_age = models.IntegerField(blank=True, null=True)
    family5_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)

    special_achievements = models.TextField(null=True, blank=True)
    interests = models.TextField('Area of interest where his/her talents can be utilized at Amity', null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)

    emergency1_name = models.CharField('Emergency Contact Person Name', max_length=120, null=True, blank=True)
    emergency1_location = models.CharField('Emergency Contact Person Location', max_length=120, null=True, blank=True)
    emergency1_phone = models.BigIntegerField(blank=True, null=True)
    emergency2_name = models.CharField('Emergency Contact Person Name', max_length=120, null=True, blank=True)
    emergency2_location = models.CharField('Emergency Contact Person Location', max_length=120, null=True, blank=True)
    emergency2_phone = models.BigIntegerField(blank=True, null=True)

    date_updated = models.DateField(auto_now=True)


    def __unicode__(self):
        return '%s' %self.student

    def get_absolute_url(self):
        return reverse('mentee_detail', kwargs={'pk': self.id})


class Meeting(models.Model):
    mentor = models.ForeignKey(Mentor)
    mentee = models.ForeignKey(Mentee)
    date = models.DateField()
    remarks = models.TextField(null=True, blank=True)
    session = models.ForeignKey(Session)

    class Meta:
        permissions = (
                ('view_meeting', 'Can view Meeting'),
                )

    def __unicode__(self):
        return '%s - %s on %s' %(self.mentor.faculty.user.first_name, self.mentee, self.date)

    def get_absolute_url(self):
        return reverse('meeting_detail', kwargs={'pk': self.id})
