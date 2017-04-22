#!/usr/bin/env python
# coding=utf-8
"""

__created__ =  2017/4/22 11:22
__author__ = 'baishaohua'
# @Site    : www.nginxs.net
"""


from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/$', views.Task_list, name='Task_list'),
    url(r'^exec/(?P<id>\d+)/$', views.Task_exec, name='Task_exec'),
    url(r'^log_list/(?P<id>\d+)/$', views.Task_log_list, name='Task_log_list'),
    url(r'^log/(?P<id>\d+)/$', views.Task_log, name='Task_log'),
]
