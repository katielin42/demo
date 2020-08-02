from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Newsletter
# Create your views here.

# displays all newsletters
def allposts(request):
    # order by latest
    posts = Newsletter.objects.order_by('-publication')
    pageTitle = "Newsletters"
    tabTitle = "Newsletters"
    return render(request, 'allposts.html', {"posts": posts, "pageTitle": pageTitle, "tabTitle": tabTitle})

# displays posts based on query from the search bar
def filteredposts(request):
    searchQuery = request.GET.get('query','')
    posts = Newsletter.objects.filter(body__contains=searchQuery).order_by('-publication')
    pageTitle = "Searching for " + searchQuery
    tabTitle = searchQuery + " results"
    if(posts.count() == 0):
        pageTitle ="No results found for " + searchQuery
    return render(request, 'allposts.html', {"posts": posts, "pageTitle": pageTitle, "tabTitle":tabTitle})

# displays the page in more detail
def detail(request, post_id):
    detail_blog = get_object_or_404(Newsletter, pk=post_id)
    if detail_blog == Http404:
        print("error msg")
        return render(request, 'error.html')
    try:
        detail_blog = Newsletter.objects.get(pk=post_id)
        return render(request, 'detail.html', {"post": detail_blog})
    except Newsletter.DoesNotExist:
        return render(request, 'error.html')


