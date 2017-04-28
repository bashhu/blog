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
    url(r'^$', views.Task_listView.as_view(), name='Task_list'),
    url(r'^exec/(?P<id>\d+)/$', views.Task_exec, name='Task_exec'),
    url(r'^log_list/(?P<id>\d+)/$', views.Task_log_list, name='Task_log_list'),
    url(r'^log/(?P<id>\d+)/$', views.Task_log, name='Task_log'),
    url(r'^cmd/$', views.Task_cmd, name='Task_cmd'),
    url(r'^cmd/online$', views.Cmd_online, name='Cmd_online'),
]
