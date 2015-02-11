from django.conf.urls import patterns, url
from versioncontrol import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
