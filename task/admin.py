from django.contrib import admin
from task.models import Command,Command_log
# Register your models here.
admin.site.register(Command)
admin.site.register(Command_log)