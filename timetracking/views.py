from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeLog

def index(request):
    report = TimeLog.objects.order_by("-date")[:5]
    output = ",".join([str(time.duration) for time in report])
    return HttpResponse(output)
