from django.contrib import admin
from academics.models import Course, Subject, Section, Teach, Performance

class TeachAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'section', 'subject')

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'sessional1', 'sessional2', 'quiz', 'attendance')

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Teach, TeachAdmin)
admin.site.register(Performance, PerformanceAdmin)
