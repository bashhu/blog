# coding=utf-8
"""

__created__ =  2017/5/17 16:15
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""

from django.conf.urls import include, url
from django.contrib import admin
from esweb import views


urlpatterns = [
    url(r'^$', views.Home, name = 'index'),
#    url(r'^cluster/$', views.cluster_status, name = 'cluster'),
    url(r'^indexs_list/$', views.indexs_list, name='indexs_list'),
    url(r'^node_list/$', views.node_list, name='node_list'),
    url(r'^info/(?P<id>\d+)/$', views.es_info, name = 'info'),
]