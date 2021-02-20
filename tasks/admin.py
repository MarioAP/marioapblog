from django.contrib import admin
from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    list_display = ("titlu", "deskrisaun",)

admin.site.register(TaskModel, TaskAdmin)
