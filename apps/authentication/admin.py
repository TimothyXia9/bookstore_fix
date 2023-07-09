from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group
#取消显示组
admin.site.unregister(Group)