# coding=utf-8
"""

__created__ = '16/9/15'
__author__ = 'deling.ma'
"""
#from utils.processing import salt_machine_sync
from django.contrib import admin
from asset.models import Machine, IdcAsset, NetworkAsset, MachineGroup, ServiceGroup
from asset.forms import MachineForm


class MachineAdmin(admin.ModelAdmin):
    list_display = ["id", "hostname", "ip", "m_group", "get_s_group", "virtual", "os", "cpu_groups", "cpu_nums", "mem",
                    "status"]
    list_display_links = ["id", "hostname"]
    form = MachineForm

    def get_s_group(self, obj):
        return "\n".join([p.name for p in obj.s_group.all()])
    get_s_group.short_description = "业务服务组"
from django.contrib import admin
admin.site.register(Machine, MachineAdmin)


class IdcAssetAdmin(admin.ModelAdmin):
    list_display = ["id", "idc_name", "idc_location", "idc_contacts", "business_contacts", "service_contacts", "contract_date"]
    list_display_links = ["id", "idc_name"]

admin.site.register(IdcAsset, IdcAssetAdmin)


class NetworkAssetAdmin(admin.ModelAdmin):
    list_display = ["id", "hostname", "manufacturer", "productname",
                    "idc_jg", "service_tag"]
    list_display_links = ["id", "hostname"]

admin.site.register(NetworkAsset, NetworkAssetAdmin)


class MachineGroupAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "remark"]
    list_display_links = ["id", "name"]

admin.site.register(MachineGroup, MachineGroupAdmin)


class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "remark"]
    list_display_links = ["id", "name"]


admin.site.register(ServiceGroup, ServiceGroupAdmin)
