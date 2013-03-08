from django.contrib import admin
from mentor_system.models import Mentor, Meeting, Mentee

class MentorAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'section', 'group')
    search_fields = ['faculty', 'section']

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'date')

admin.site.register(Mentee)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Meeting, MeetingAdmin)
