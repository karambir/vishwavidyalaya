from django.contrib import admin
from profiles.models import Faculty, Student, Director

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('empID', 'user', 'designation')
    search_fields = ['empId' ,'designation', 'qualification', 'experience']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_number', 'first_name', 'last_name', 'course', 'section')
    search_fields = ['first_name', 'last_name', 'email', 'form_number', 'enrollment_number']

admin.site.register(Director)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
