from django.contrib import admin
from mentors.models import Mentor, MenteeMeeting, Mentee

class MentorAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'section', 'group')
    search_fields = ['faculty', 'section']

class MenteeMeetingAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'date')

admin.site.register(Mentee)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(MenteeMeeting, MenteeMeetingAdmin)
