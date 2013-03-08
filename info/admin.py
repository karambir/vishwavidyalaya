from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'title', 'created_at')

admin.site.register(News, NewsAdmin)
