from django.contrib import admin
from .models import Project, Task, TimeLog,WeeklyTarget
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TimeLog)
admin.site.register(WeeklyTarget)