from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

from vishwavidyalaya.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vishwavidyalaya.views.home', name='home'),
    # url(r'^vishwavidyalaya/', include('vishwavidyalaya.foo.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^school/', include('school.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='user_profile'),
    #url(r'^mentee/', include('mentors.urls')),
    url(r'^profiles/', include('profiles.urls')),
    #url(r'^academics/', include('academics.urls')),
    #url(r'^news/', include('news.urls')),

)
