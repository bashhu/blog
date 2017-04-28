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
from article import views

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^task/', include('task.urls', namespace='task')),
    url(r'^users/', include('accounts.urls', namespace='user')),
    url(r'^article/',include('article.urls', namespace='article')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Indexview.as_view(), name = 'home'),
]
