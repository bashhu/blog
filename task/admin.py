#coding:utf-8
from django.contrib import admin
from task.models import Command,Command_log
from django.contrib.auth.models import Group, Permission
# Register your models here.
class CommandAdmin(admin.ModelAdmin):
    list_display = ('cmd_name', 'cmd_cate','salt_mod')
    actions = ['make_pro']

    def make_pro(self, request, queryset):
        queryset.update(cmd_cate='生产环境')

    make_pro.short_description = "Mark selected stories as 生产环境"
    #permission = Permission.objects.create(exec_task='exec_task', change_task='change_task', add_task='add_task')

class Command_logAdmin(admin.ModelAdmin):
    list_display = ('cmd_name', 'cmd_cate','salt_mod','salt_reason','salt_res')

admin.site.register(Command,CommandAdmin)
admin.site.register(Command_log,Command_logAdmin)