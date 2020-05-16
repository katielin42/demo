from django.shortcuts import render
from .models import Team

#testing the page
team = Team.objects.all()

def home(request):
    return render(request, 'team.html', {"team": team})

def club(request):
    return render(request, 'club.html', {"team": team})

# Create your views here.
