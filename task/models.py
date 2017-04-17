#coding:utf-8
from django.db import models

# Create your models here.
# Create your models here.
class Command(models.Model) :
    cmd_name = models.CharField(max_length = 100)  #题目
    cmd_cate = models.CharField(max_length = 50, blank = True)  #命令标签
    ctime = models.DateTimeField(auto_now_add = True)  #命令创建时间
    salt_mod = models.CharField(max_length = 50)  #salt模块
    salt_host =  models.CharField(max_length = 50)  #管理的主机
    salt_parm_c = models.BooleanField(default=True)
    salt_parm = models.CharField(max_length = 50)

    ''' get url an reverse to you want'''

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.cmd_name

    class Meta:  #按时间下降排序
        ordering = ['-ctime']

class Command_log(models.Model) :
    '''记录执行记录和结果'''
    task_id = models.IntegerField(max_length = 100)
    cmd_name = models.CharField(max_length = 100)  #题目
    cmd_cate = models.CharField(max_length = 50, blank = True)  #命令标签
    etime = models.DateTimeField(auto_now_add = True)  #命令执行时间
    salt_mod = models.CharField(max_length = 50)  #salt模块
    salt_host =  models.CharField(max_length = 50)  #管理的主机
    salt_parm = models.CharField(max_length = 50,null = True)
    salt_res = models.TextField(blank = True, null = True) #执行结果
    salt_reason = models.TextField(blank=True, null=True)  # 执行原因

    ''' get url an reverse to you want'''

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.cmd_name

    class Meta:  #按时间下降排序
        ordering = ['-etime']