from django.contrib import admin
from . import models

@admin.register(models.ToDo)
class ToDoAdmin(admin.ModelAdmin):
    pass