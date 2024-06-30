from django.contrib import admin

from webapp.models import TaskManage


class TaskManageAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'deadline']


# Register your models here.

admin.site.register(TaskManage, TaskManageAdmin)
