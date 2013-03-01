from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vishwavidyalaya.views.home', name='home'),
    # url(r'^vishwavidyalaya/', include('vishwavidyalaya.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
