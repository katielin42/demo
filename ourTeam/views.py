from django.shortcuts import render
from django.http import HttpResponse

#testing the page
def home(request):
    return HttpResponse('<h1> blog home </h1>')

# Create your views here.
