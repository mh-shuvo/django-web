from django.db import models
from django.utils import timezone
from django.db import models
from django.db.models import Sum
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    details = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(blank=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-project_id"]
    
    def __str__(self):
        return self.name;

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=50)
    assigne = models.CharField(max_length=70)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(blank=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-task_id"]
    
    def __str__(self):
        return f"{self.project.name}: {self.title}";


class TimeLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(blank=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-log_id"]

    def __str__(self):
        return f"{self.task.title}({self.duration} hours) on {self.date}"


    @classmethod
    def get_task_durations(cls):
        task_durations = cls.objects.values(
            'task__task_id', 
            'task__project__name', 
            'task__title', 
            'task__assigne'
        ).annotate(
            total_duration=Sum('duration')
        )
        return task_durations