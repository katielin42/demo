from django.shortcuts import render

from .models import Job
# Create your views here.

def home(request):
    # get the jobs from model, pass to be returned
    jobs= Job.objects
    return render(request, 'home.html', {'jobs':jobs})

def team(request):
    return render(request,'team.html')