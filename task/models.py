#coding:utf-8
from django.db import models
from django.contrib.auth.models import Permission, User

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

    class Meta:
        permissions = (
            ("exec_task", "Can exec available tasks"),
            ("change_task", "Can change the status of tasks"),
            ("add_task", "add a task"),
        )
    ''' get url an reverse to you want'''
    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.cmd_name

    class Meta:  #按时间下降排序
        ordering = ['-ctime']


class Command_log(models.Model) :
    '''记录执行记录和结果'''
    task_id = models.IntegerField()
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

class Crontab(models.Model) :
    con_name = models.CharField(max_length = 100)  #题目
    con_cate = models.CharField(max_length = 50, blank = True)  #命令标签
    ctime = models.DateTimeField(auto_now_add = True)  #命令创建时间
    con_cmd = models.CharField(max_length = 250)  #salt模块
    con_time =  models.CharField(max_length = 250)  #管理的主机
    con_user = models.CharField(max_length=50)  # 执行定时任务用户
    utime = models.DateTimeField(auto_now_add=True) #更新任务最近时间

    ''' get url an reverse to you want'''

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.con_name

    class Meta:  #按时间下降排序
        ordering = ['-ctime']