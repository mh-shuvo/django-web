from django.db import models
from django.utils import timezone
from django.db import models
from django.db.models import Sum
from django.utils.timezone import now
from datetime import date, timedelta
from django.contrib.auth.models import User

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
    # assigne = models.CharField(max_length=70)
    assigne = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,default=1)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(blank=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-task_id"]
    
    def __str__(self):
        return f"{self.project.name}: {self.title}";
    @classmethod
    def get_info_by_id(cls,id):
        return cls.objects.filter(task_id=id).first()


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
    def get_task_durations(cls,user_id):
        current_date = now().date()
        task_durations = cls.objects.filter(
            date = current_date
        ).filter(task__assigne=user_id).values(
            'task__task_id', 
            'task__project__name', 
            'task__title'
        ).annotate(
            total_duration=Sum('duration')
        )
        return task_durations
    
    @classmethod
    def get_task_time_logs_by_id(cls,id):
        tasks = cls.objects.filter(task_id=id).all()
        return tasks
    
    @classmethod
    def get_all_task_durations(cls,user_id):
        task_durations = cls.objects.filter(task__assigne = user_id).values(
            'task__task_id', 
            'task__project__name', 
            'task__title'
        ).annotate(
            total_duration=Sum('duration')
        ).order_by('-log_id')
        return task_durations
    
    @classmethod
    def get_current_week_work_duration(cls,user_id):
        today = date.today()
        # Calculate the start of the week (Saturday)
        start_of_week = today - timedelta(days=(today.weekday() + 2) % 7)
        # Calculate the end of the week (Friday)
        end_of_week = start_of_week + timedelta(days=6)

        # Query the total duration for this week
        total_duration = TimeLog.objects.filter(
            date__range=(start_of_week, end_of_week)
        ).filter(task__assigne = user_id).aggregate(total=Sum('duration'))['total']

        return total_duration

    @classmethod
    def get_today_total_work_duration(cls,user_id):
        
        current_date = now().date()
        
        total_duration = cls.objects.filter(date=current_date).filter(task__assigne = user_id).aggregate(total_duration=Sum('duration'))['total_duration']
        return total_duration or 0
    
    @classmethod
    def get_current_month_work_duration(cls, user_id):
        today = now().date()
        start_of_month = today.replace(day=1)
        total_duration = cls.objects.filter(
            date__range=(start_of_month, today),
            task__assigne=user_id
        ).aggregate(total_duration=Sum('duration'))['total_duration']
        return total_duration or 0

    @classmethod
    def get_current_year_work_duration(cls, user_id):
        today = now().date()
        start_of_year = today.replace(month=1, day=1)
        total_duration = cls.objects.filter(
            date__range=(start_of_year, today),
            task__assigne=user_id
        ).aggregate(total_duration=Sum('duration'))['total_duration']
        return total_duration or 0