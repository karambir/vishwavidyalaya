from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vishwavidyalaya.views.home', name='home'),
    # url(r'^vishwavidyalaya/', include('vishwavidyalaya.foo.urls')),

    (r'^$', TemplateView.as_view(template_name = 'base.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/profile/$', TemplateView.as_view(template_name = 'profile.html')),

)
