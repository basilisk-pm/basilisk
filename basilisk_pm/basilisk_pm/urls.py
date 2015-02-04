from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'basilisk_pm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
