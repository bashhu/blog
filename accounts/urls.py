# coding=utf-8
"""

__created__ =  2017/4/24 18:19
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""


from django.conf.urls import include, url
from django.contrib import admin
from accounts import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.accounts, name = 'home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^list/$', views.user_list, name='user_list'),
    url(r'^$', views.accounts, name='accounts'),
]
