from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<project_id>\d+)/code/$', views.code, name='code'),
    url(r'^(?P<project_id>\d+)/calendar/$', views.calender, name='calender'),
    url(r'^(?P<project_id>\d+)/gantt/$', views.gantt, name='gantt'),
    url(r'^(?P<project_id>\d+)/files/$', views.files, name='files'),
    url(r'^(?P<project_id>\d+)/settings/$', views.settings, name='settings'),
    url(r'^new-project/$', views.new_project, name='new-project'),
)
