from django.conf.urls import patterns, url
from bugs import views

urlpatterns = patterns('',
    url(r'^(?P<project_id>\d+)/$', views.index, name='index'),
    url(r'^(?P<project_id>\d+)/new-issue/$', views.new_issue, name='new-issue'),
    url(r'^(?P<project_id>\d+)/issues/$', views.all_issues, name='issues'),
    url(r'^(?P<project_id>\d+)/issues/(?P<bug_id>\d+)/$', views.view_issue, name='issue'),
)
