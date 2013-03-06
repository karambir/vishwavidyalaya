from django.db import models
from profiles.models import Faculty

from django.core.urlresolvers import reverse

class News(models.Model):
    faculty = models.ForeignKey(Faculty)
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.id})
