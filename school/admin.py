from django.contrib import admin
from school.models import School, Department, Course, Subject, Section, Session

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'university')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'coordinator')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'batch', 'school')

admin.site.register(Course, CourseAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Session)
