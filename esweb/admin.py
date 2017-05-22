#coding:utf-8
from django.contrib import admin
from esweb.models import ES

# Register your models here.
class ESAdmin(admin.ModelAdmin):
    list_display = ('project', 'hostname', 'ip','port')

admin.site.register(ES,ESAdmin)
