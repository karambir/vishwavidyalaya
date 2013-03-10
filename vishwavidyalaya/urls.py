from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vishwavidyalaya.views.home', name='home'),
    # url(r'^vishwavidyalaya/', include('vishwavidyalaya.foo.urls')),

    (r'^$', TemplateView.as_view(template_name = 'index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^school/', include('school.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/profile/$', login_required(TemplateView.as_view(template_name = 'profile.html'))),
    #url(r'^mentee/', include('mentors.urls')),
    #url(r'^profiles/', include('profiles.urls')),
    #url(r'^academics/', include('academics.urls')),
    #url(r'^news/', include('news.urls')),

)
