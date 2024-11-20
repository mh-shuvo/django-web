from django.contrib import admin
from .models import TimeLog,Project,Task
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TimeLog)