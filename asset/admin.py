# coding=utf-8
"""

__created__ = '16/9/15'
__author__ = 'deling.ma'
"""
#from utils.processing import salt_machine_sync
import admin
from asset.models import Machine, IdcAsset, NetworkAsset, MachineGroup, ServiceGroup
from asset.forms import MachineForm


class SaltSyncAction(BaseActionView):
    actions_selection_counter = False
    # 这里需要填写三个属性
    action_name = "salt_sync_machine"
    # 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = "重新同步"
    action_across = True
    model_perm = 'change'    #: 该 Action 所需权限

    # 而后实现 do_action 方法
    def do_action(self, queryset=None):
        # queryset 是包含了已经选择的数据的 queryset
        #result = salt_machine_sync()
        result = 'test.dianjoy.com'
        self.message_user("同步结果: <pre>%s</pre>" % result)


class MachineAdmin(object):
    list_display = ["id", "hostname", "ip", "m_group", "get_s_group", "virtual", "os", "cpu_groups", "cpu_nums", "mem",
                    "status"]
    list_display_links = ["id", "hostname"]
    actions = [SaltSyncAction, ]
    form = MachineForm

    def get_s_group(self, obj):
        return "\n".join([p.name for p in obj.s_group.all()])
    get_s_group.short_description = "业务服务组"

admin.site.register(Machine, MachineAdmin)


class IdcAssetAdmin(object):
    list_display = ["id", "idc_name", "idc_location", "idc_contacts", "business_contacts", "service_contacts", "contract_date"]
    list_display_links = ["id", "idc_name"]

admin.site.register(IdcAsset, IdcAssetAdmin)


class NetworkAssetAdmin(object):
    list_display = ["id", "hostname", "manufacturer", "productname",
                    "idc_jg", "service_tag"]
    list_display_links = ["id", "hostname"]

admin.site.register(NetworkAsset, NetworkAssetAdmin)


class SourceBackupAdmin(object):
    list_display = ["id", "hostname", "source", "b_type",
                    "ip", "size", "backup_date", "start", "end"]
    list_display_links = ["id", "hostname"]
    list_filter = ["backup_date", "ctime", "b_type"]
    search_fields = ["hostname", "ip"]

admin.site.register(SourceBackup, SourceBackupAdmin)


class MachineGroupAdmin(object):
    list_display = ["id", "name", "remark"]
    list_display_links = ["id", "name"]

admin.site.register(MachineGroup, MachineGroupAdmin)


class ServiceGroupAdmin(object):
    list_display = ["id", "name", "remark"]
    list_display_links = ["id", "name"]


admin.site.register(ServiceGroup, ServiceGroupAdmin)
