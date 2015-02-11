from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import projects, profiles, bugs, versioncontrol



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'basilisk_pm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='project-list.html')),
    url(r'^projects/', include('projects.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^bugs/', include('bugs.urls')),
    url(r'^versioncontrol/', include('versioncontrol.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

