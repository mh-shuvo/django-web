from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    template = loader.get_template("moderator/home.html")
    return HttpResponse(template.render({},request))