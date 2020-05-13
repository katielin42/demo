from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Newsletter
# Create your views here.


def allposts(request):
    posts = Newsletter.objects.order_by('-publication') # display by latest
    #posts = Newsletter.objects

    pageTitle = "Newsletter"
    tabTitle = "Newsletter"
    return render(request, 'allposts.html', {"posts": posts, "pageTitle": pageTitle, "tabTitle": tabTitle})

def render_to_response(param):
    pass

def filteredposts(request):
    searchQuery = request.GET.get('query','')
    print("test query")
    print(searchQuery)
    posts = Newsletter.objects.filter(body__contains=searchQuery).order_by('-publication')
    pageTitle = "Searching for " + searchQuery
    tabTitle = searchQuery + " results"
    if(posts.count() == 0):
        pageTitle ="No results found for " + searchQuery
    #posts = Newsletter.objects.order_by('-publication') # display by latest

    return render(request, 'allposts.html', {"posts": posts, "pageTitle": pageTitle, "tabTitle":tabTitle})

def detail(request, post_id):
    detail_blog = get_object_or_404(Newsletter, pk=post_id)
    if detail_blog == Http404:
        print("error msg")
        return render(request, 'error.html')
    print("here")

    try:
        detail_blog = Newsletter.objects.get(pk=post_id)
        return render(request, 'detail.html', {"post": detail_blog})
    except Newsletter.DoesNotExist:
        return render(request, 'error.html')


