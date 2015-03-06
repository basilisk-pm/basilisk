from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<project_id>\d+)/code/$', views.code, name='code'),
    url(r'^(?P<project_id>\d+)/files/$', views.files, name='files'),
    url(r'^(?P<project_id>\d+)/settings/$', views.settings, name='settings'),
)
