# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.core.urlresolvers import reverse

# definition of UserProfile from above
class User(models.Model) :
    username = models.CharField(max_length = 100)  #题目
    ctime = models.DateTimeField(auto_now_add = True)  #命令创建时间
    permissions = (("can_deliver_pizzas", "Can deliver pizzas"),)

    #class Meta:

    ''' get url an reverse to you want'''
    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.username

    class Meta:  #按时间下降排序
        ordering = ['-ctime']


class Group(models.Model) :
    groupname = models.CharField(max_length = 100)  #题目
    ctime = models.DateTimeField(auto_now_add = True)  #命令创建时间


    class Meta:
        permissions = (
            ("guest", "Can access public msg"),
            ("user", "Can access private msg"),
            ("admin", "all privilege"),
        )