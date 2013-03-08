from django.contrib import admin
from info.models import News, FacultyTimeTable

class NewsAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'title')

class FacultyTimeTableAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'class_type', 'section', 'subject', 'weekday', 'number')

admin.site.register(News, NewsAdmin)
admin.site.register(FacultyTimeTable, FacultyTimeTableAdmin)
