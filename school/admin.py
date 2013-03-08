from django.contrib import admin
from school.models import School, Department, Course, Subject, Section, Session

admin.site.register(Course)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Session)
