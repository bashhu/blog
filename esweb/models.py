#coding:utf-8
from django.db import models

# Create your models here.
class ES(models.Model) :
    project = models.CharField(max_length=50)  # 项目
    hostname = models.CharField(max_length=50)
    ip = models.CharField(max_length = 100)  #ip
    port = models.CharField(max_length = 5, default = 9200)  #端口
    ctime = models.DateTimeField(auto_now_add = True)  #命令创建时间

    class Meta:
        permissions = (
            ("es_search", "Can Search docs"),
            ("es_write", "Can update docs"),
            ("es_delete", "delete same index"),
        )
    ''' get url an reverse to you want'''
    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.ip

    class Meta:  #按时间下降排序
        ordering = ['-ctime']