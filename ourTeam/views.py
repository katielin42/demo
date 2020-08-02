from django.shortcuts import render
from .models import Team

# returns the team members separately as sr and jr execs
def team(request):
    jrexecs = Team.objects.filter(isSenior=False)
    srexecs = Team.objects.filter(isSenior=True)
    return render(request, 'team.html', {"jrexecs": jrexecs, "srexecs":srexecs})

# returns the team members separately as jr and senior execs, removing duplicates
def club(request):
    jrexecs = Team.objects.filter(isSenior=False,isDuplicateDescription=False)
    srexecs = Team.objects.filter(isSenior=True,isDuplicateDescription=False)
    return render(request, 'club.html', {"jrexecs": jrexecs, "srexecs":srexecs})


