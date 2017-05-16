# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enter/\d*/?$', views.enter, name='enter'),
    url(r'^version/\d*/?$', views.version, name='version'),
    url(r'^res/(?P<version>[.\w_-]+)/(?P<uri>.+)/$', views.res, name='res'),
    url(r'^res/(?P<uri>.+)/$', views.res, name='res'),
]
