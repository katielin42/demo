from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def club(request):
    return render(request,'club.html')

def events(request):
    return render(request, 'events.html')



