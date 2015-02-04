from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
