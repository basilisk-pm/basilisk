from django.conf.urls import patterns, url
from bugs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'new-issue/$', views.new_issue, name='new-issue'),
    url(r'issues/$', views.all_issues, name='issues'),
)
