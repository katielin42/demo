from django.shortcuts import render
from .models import Team

#testing the page
# team = Team.objects.all()


def home(request):
    jrexecs = Team.objects.filter(isFilled=True,isSenior=False)
    srexecs = Team.objects.filter(isFilled=True,isSenior=True)
    return render(request, 'team.html', {"jrexecs": jrexecs, "srexecs":srexecs})

def club(request):
    
    jrexecs = Team.objects.filter(isSenior=False,isDuplicateDescription=False)
    srexecs = Team.objects.filter(isSenior=True,isDuplicateDescription=False)
    return render(request, 'club.html', {"jrexecs": jrexecs, "srexecs":srexecs})

# Create your views here.
