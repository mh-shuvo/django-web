from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeLog,Task
from django.template import loader
from django.contrib.auth.decorators import login_required
def index(request):
    if request.user.is_authenticated is False:
        return render(request, 'welcome.html')
    
    
    current_week_duration = TimeLog.get_current_week_work_duration(request.user.id);
    report = TimeLog.get_task_durations(request.user.id)
    total_work_duration_in_today = TimeLog.get_today_total_work_duration(request.user.id)

    template = loader.get_template("index.html")
    
    return HttpResponse(template.render({
        "report": report,
        "total_work_in_today": total_work_duration_in_today,
        "total_work_in_week": current_week_duration
    },request))

@login_required(login_url='/login')
def get_working_histories(request):
    full_report = TimeLog.get_all_task_durations(request.user.id)

    template = loader.get_template("working_histories.html")
    
    return HttpResponse(template.render({
        "report": full_report,
    },request))

def history(request,id):
    report = TimeLog.get_task_time_logs_by_id(id)
    task_info = Task.get_info_by_id(id)

    template = loader.get_template("history.html")
    
    return HttpResponse(template.render({
        "report": report,
        "task_info": task_info
    },request))