# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enter/$', views.enter, name='enter'),
    url(r'^res/(?P<uri>.+)/$', views.res, name='res'),
]
