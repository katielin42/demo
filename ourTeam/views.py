from django.shortcuts import render
from django.http import HttpResponse

#testing the page
team = [{
    "name": 'name',
    "title": 'title',
    "description": 'description'
},
    {
        "name": 'name2',
        "title": 'title2',
        "description": 'description2'
    }
]


def home(request):
    return render(request, 'team.html', {'team': team})

# Create your views here.
