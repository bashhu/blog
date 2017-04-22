# coding=utf-8
"""

__created__ = '16/9/15'
__author__ = 'deling.ma'
"""
from django.db import models


class MachineGroup(models.Model):
    name = models.CharField(u"主机组名称", max_length=50)
    remark = models.TextField(u"备注", max_length=50, blank=True,
                              default='')

    class Meta:
        db_table = "machine_group"
        verbose_name = u"主机分组"
        verbose_name_plural = u"主机分组"

    def __str__(self):
        return self.name


class ServiceGroup(models.Model):
    name = models.CharField(u"业务服务组名称", max_length=50)
    remark = models.TextField(u"备注", max_length=50, blank=True,
                              default='')

    class Meta:
        db_table = "service_group"
        verbose_name = u"业务服务分组"
        verbose_name_plural = u"业务服务分组"

    def __str__(self):
        return self.name

MACHINE_STATUS_CHOICES = (
    ("up", "正常运行"),
    ("down", "已关闭"),
)


class Machine(models.Model):
    hostname = models.CharField(max_length=50, verbose_name=u'主机名', default="")
    m_group = models.ForeignKey(MachineGroup, blank=True,
                                verbose_name=u"主机分组")
    s_group = models.ManyToManyField(ServiceGroup, blank=True, null=True,
                                     verbose_name=u"业务服务组")
    ip = models.CharField(max_length=50, unique=True, verbose_name=u'IP地址')
    manufacturer = models.CharField(max_length=50, verbose_name=u'厂商',
                                    blank=True, default="")
    productname = models.CharField(max_length=50, verbose_name=u'产品型号')
    service_tag = models.CharField(max_length=80, verbose_name=u'序列号')
    cpu_model = models.CharField(max_length=50, verbose_name=u'CPU型号')
    cpu_nums = models.PositiveSmallIntegerField(verbose_name=u'CPU线程数')
    cpu_groups = models.PositiveSmallIntegerField(verbose_name=u'CPU物理核数')
    mem = models.CharField(max_length=5, verbose_name=u'内存大小')
    # macaddress = models.CharField(max_length=50, verbose_name=u'MAC地址')
    os = models.CharField(max_length=50, verbose_name=u'操作系统')
    virtual = models.CharField(verbose_name=u'主机类型', max_length=50)
    salt_control = models.BooleanField(u"是否Salt托管", default=False)
    status = models.CharField(u"节点状态", max_length=16,
                              choices=MACHINE_STATUS_CHOICES,
                              default="up")

    unique_together = ("hostname", "ip")

    class Meta:
        db_table = 'machine'
        verbose_name = u'主机管理'
        verbose_name_plural = u'主机管理'

    def __unicode__(self):
        return u'%s-%s' % (self.ip, self.hostname)

    @property
    def full_name(self):
        return u'%s-%s' % (self.ip, self.hostname)


class NetworkAsset(models.Model):
    ip = models.CharField(max_length=20, verbose_name=u'IP地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    manufacturer = models.CharField(max_length=20, verbose_name=u'厂商')
    productname = models.CharField(max_length=20, verbose_name=u'产品型号')
    idc_jg = models.CharField(max_length=10, blank=True, verbose_name=u'机柜编号')
    service_tag = models.CharField(max_length=30, unique=True,
                                   verbose_name=u'序列号')
    remark = models.TextField(max_length=50, blank=True, verbose_name=u'备注',
                              default='')

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name = u'网络设备'
        verbose_name_plural = u'网络设备'


class IdcAsset(models.Model):
    idc_name = models.CharField(max_length=20, verbose_name=u'机房名称')
    idc_type = models.CharField(max_length=20, verbose_name=u'机房类型')
    idc_location = models.CharField(max_length=30, verbose_name=u'机房位置')
    contract_date = models.DateTimeField(verbose_name=u'合同到期时间',blank=True)
    idc_contacts = models.CharField(max_length=30, verbose_name=u'机房值班电话')
    business_contacts = models.CharField(max_length=30, verbose_name=u'商务联系人',default='')
    service_contacts = models.CharField(max_length=30, verbose_name=u'客服联系人',default='')
    remark = models.TextField(max_length=50, blank=True, verbose_name=u'备注',
                              default='')

    def __unicode__(self):
        return self.idc_name

    class Meta:
        verbose_name = u'机房管理'
        verbose_name_plural = u'机房管理'

