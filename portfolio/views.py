from django.shortcuts import render


def home(request):
    # get the jobs from model, pass to be returned
    return render(request, 'home.html')


# def team(request):
#     return render(request,'team.html')

def club(request):
    return render(request,'club.html')

def events(request):
    return render(request, 'events.html')

def test(request):
    return render(request, 'test.html')


