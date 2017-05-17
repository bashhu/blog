from django.contrib import admin
from accounts.models import User
# Register your models here.
# which acts a bit like a singleton
admin.site.register(User)