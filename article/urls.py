# coding=utf-8
"""

__created__ =  2017/4/27 14:34
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views


urlpatterns = [
    url(r'^$', views.Indexview.as_view(), name = 'index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^archives/$', views.ArchView.as_view(), name = 'archives'),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.Search_tagView.as_view(), name = 'search_tag'),
    url(r'^search/$', views.blog_search, name = 'search'),
]

