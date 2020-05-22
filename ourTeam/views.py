from django.shortcuts import render
from .models import Team

#testing the page
# team = Team.objects.all()
jrexecs = Team.objects.filter(isSenior=False)
srexecs = Team.objects.filter(isSenior=True)

def home(request):
    return render(request, 'team.html', {"jrexecs": jrexecs, "srexecs":srexecs})

def club(request):
    return render(request, 'club.html', {"jrexecs": jrexecs, "srexecs":srexecs})

# Create your views here.
