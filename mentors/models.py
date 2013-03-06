from django.db import models
from profiles.models import Faculty, Student
from academics.models import Section

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Student)
def mentee_creation(sender, instance, created, **kwargs):
    mentee = Mentee(student=instance)
    mentee.save()


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


class Mentee(models.Model):
    student = models.ForeignKey(Student)

    present_address_street = models.CharField(max_length=350, blank=True, null=True)
    present_address_city = models.CharField(max_length=100, null=True, blank=True)
    present_address_state = models.CharField(max_length=30, null=True, blank=True)
    present_address_pincode = models.IntegerField(null=True, blank=True)
    present_address_phone = models.BigIntegerField(blank=True, null=True)
    present_address_email = models.EmailField(blank=True, null=True)

    permanent_address_street = models.CharField(max_length=350, blank=True, null=True)
    permanent_address_city = models.CharField(max_length=100, null=True, blank=True)
    permanent_address_state = models.CharField(max_length=30, null=True, blank=True)
    permanent_address_pincode = models.IntegerField(null=True, blank=True)
    permanent_address_phone = models.BigIntegerField(blank=True, null=True)
    permanent_address_email = models.EmailField(blank=True, null=True)

    local_guardian_name = models.CharField(max_length=120, null=True, blank=True)
    local_guardian_address = models.CharField(max_length=350, null=True, blank=True)
    local_guardian_phone = models.BigIntegerField(blank=True, null=True)
    local_guardian_email = models.EmailField(blank=True, null=True)

    school_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    school_year = models.IntegerField(null=True, blank=True)
    school_division = models.IntegerField(null=True, blank=True)
    school_remarks = models.CharField(max_length=350, null=True, blank=True)

    inter_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    inter_year = models.IntegerField(null=True, blank=True)
    inter_division = models.IntegerField(null=True, blank=True)
    inter_remarks = models.CharField(max_length=350, null=True, blank=True)

    degree_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    degree_year = models.IntegerField(null=True, blank=True)
    degree_division = models.IntegerField(null=True, blank=True)
    degree_remarks = models.CharField(max_length=350, null=True, blank=True)

    others_board = models.CharField('Board/University', max_length=350, null=True, blank=True)
    others_year = models.IntegerField(null=True, blank=True)
    others_division = models.IntegerField(null=True, blank=True)
    others_remarks = models.CharField(max_length=350, null=True, blank=True)

    family_member1_name = models.CharField(max_length=120, blank=True, null=True)
    family_member1_relationship = models.CharField(max_length=20, null=True, blank=True, default='Father')
    family_member1_age = models.IntegerField(blank=True, null=True)
    family_member1_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)

    family_member2_name = models.CharField(max_length=120, blank=True, null=True)
    family_member2_relationship = models.CharField(max_length=20, null=True, blank=True, default='Mother')
    family_member2_age = models.IntegerField(blank=True, null=True)
    family_member2_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)

    family_member3_name = models.CharField(max_length=120, blank=True, null=True)
    family_member3_relationship = models.CharField(max_length=20, null=True, blank=True, default='Brother')
    family_member3_age = models.IntegerField(blank=True, null=True)
    family_member3_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)
    family_member4_name = models.CharField(max_length=120, blank=True, null=True)
    family_member4_relationship = models.CharField(max_length=20, null=True, blank=True, default='Brother')
    family_member4_age = models.IntegerField(blank=True, null=True)
    family_member4_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)

    family_member5_name = models.CharField(max_length=120, blank=True, null=True)
    family_member5_relationship = models.CharField(max_length=20, null=True, blank=True, default='Sister')
    family_member5_age = models.IntegerField(blank=True, null=True)
    family_member5_qualification = models.CharField('Qualification/Occupation', max_length=150, blank=True, null=True)

    special_achievements = models.TextField(null=True, blank=True)
    interests = models.TextField('Area of interest where his/her talents can be utilized at Amity', null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True)

    emergency_name = models.CharField('Emergency Contact Person Name', max_length=120, null=True, blank=True)
    emergency_location = models.CharField('Emergency Contact Person Location', max_length=120, null=True, blank=True)
    emergency_phone = models.BigIntegerField(blank=True, null=True)

    date_updated = models.DateField(auto_now=True)

    def get_permanent_address(self):
        return '%s, %s, %s - %d' %(self.permanent_address_street, self.permanent_address_city, self.permanent_address_state, self.permanent_address_pincode)

    def get_present_address(self):
        return '%s, %s, %s - %d' %(self.present_address_street, self.present_address_city, self.present_address_state, self.present_address_pincode)

    def __unicode__(self):
        return '%s' %self.student

    def get_absolute_url(self):
        return reverse('mentee_detail', kwargs={'pk': self.id})


class MenteeMeeting(models.Model):
    mentor = models.ForeignKey(Mentor)
    mentee = models.ForeignKey(Mentee)
    date = models.DateField()
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        permissions = (
                ('view_menteemeeting', 'Can view Meeting'),
                )

    def __unicode__(self):
        return '%s - %s on %s' %(self.mentor.faculty.user.first_name, self.mentee, self.date)

    def get_absolute_url(self):
        return reverse('mentee_meeting_detail', kwargs={'pk': self.id})
