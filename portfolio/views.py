from django.shortcuts import render


def home(request):
    # get the jobs from model, pass to be returned
    return render(request, 'home.html')

def team(request):
    return render(request,'team.html')