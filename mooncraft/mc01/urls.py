# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enter/\d*/?$', views.enter, name='enter'),
    url(r'^res/(?P<version>[.\w_-]+)/(?P<uri>.+)/\d*/?$', views.res, name='res'),
]
