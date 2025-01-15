from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeLog,Task,WeeklyTarget
from django.template import loader
from django.contrib.auth.decorators import login_required
from .helper import get_current_week_start_end_date
from datetime import datetime
def index(request):
    if request.user.is_authenticated is False:
        return render(request, 'welcome.html')
    
    
    current_week_duration = TimeLog.get_current_week_work_duration(request.user.id);
    report = TimeLog.get_task_durations(request.user.id)
    total_work_duration_in_today = TimeLog.get_today_total_work_duration(request.user.id)

    template = loader.get_template("index.html")
    
    current_week = WeeklyTarget.get_weekly_data_by_date(user_id=request.user.id)
    start_of_week = current_week.week_start
    end_of_week = current_week.week_end
    target_duration = current_week.target_hours

    return HttpResponse(template.render({
        "report": report,
        "total_work_in_today": total_work_duration_in_today,
        "total_work_in_week": current_week_duration,
        "start_of_week": start_of_week,
        "end_of_week": end_of_week,
        "target_duration": target_duration
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

@login_required(login_url='/login')
def get_daily_report(request):
    date = request.GET.get('date')
    date = datetime.strptime(date, '%Y-%m-%d').date() if date else None  
    report = TimeLog.get_daily_report(request.user.id,date=date)

    template = loader.get_template("daily_report.html")
    
    return HttpResponse(template.render({
        "report": report,
    },request))