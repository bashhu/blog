#coding:utf-8
"""itblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from article import views
from article.views import RSSFeed
#from task.views import  alist,Task_exec,Task_list, Task_log, Task_log_list
from accounts import views as user1

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('users.urls')),
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name = 'detail'),
    url(r'^archives/$', views.archives, name = 'archives'),
    url(r'^aboutme/$', views.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    url(r'^search/$', views.blog_search, name = 'search'),
    url(r'^search/$', views.blog_search, name = ''),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
    url(r'^users/login/$', user1.user_login, name='login'),
    url(r'^users/logout/$', user1.user_logout, name='logout'),
    url(r'^users/list/$', user1.user_list, name='user_list'),
    url(r'^users/$', user1.accounts, name='accounts'),
]
