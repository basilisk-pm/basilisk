from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'basilisk_pm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('projects.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

