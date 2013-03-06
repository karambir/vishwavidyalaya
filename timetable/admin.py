from django.contrib import admin
from timetable.models import TimeTable

class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'section', 'weekday', 'number', 'subject')

admin.site.register(TimeTable, TimeTableAdmin)
