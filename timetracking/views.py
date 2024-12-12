from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeLog,Task
from django.template import loader
def index(request):
    
    current_week_duration = TimeLog.get_current_week_work_duration();
    report = TimeLog.get_task_durations()
    total_work_duration_in_today = TimeLog.get_today_total_work_duration()
    full_report = TimeLog.get_all_task_durations()

    template = loader.get_template("index.html")
    
    return HttpResponse(template.render({
        "report": report,
        "full_report": full_report,
        "total_work_in_today": total_work_duration_in_today,
        "total_work_in_week": current_week_duration
    },request))

def history(request,id):
    report = TimeLog.get_task_time_logs_by_id(id)
    task_info = Task.get_info_by_id(id)

    template = loader.get_template("history.html")
    
    return HttpResponse(template.render({
        "report": report,
        "task_info": task_info
    },request))