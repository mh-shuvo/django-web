from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeLog
from django.template import loader
def index(request):
    
    report = TimeLog.get_task_durations()

    template = loader.get_template("index.html")
    
    return HttpResponse(template.render({
        "report": report
    },request))