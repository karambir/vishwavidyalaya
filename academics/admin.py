from django.contrib import admin
from academics.models import FacultyAssign, Performance

class FacultyAssignAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'section', 'subject')

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'sessional1', 'sessional2', 'quiz', 'attendance')

admin.site.register(FacultyAssign, FacultyAssignAdmin)
admin.site.register(Performance, PerformanceAdmin)
