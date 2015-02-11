from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'code/$', views.code, name='code'),
    url(r'files/$', views.files, name='files'),
    url(r'settings/$', views.settings, name='settings'),
)
