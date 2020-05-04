from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Newsletter
# Create your views here.


def allposts(request):
    posts = Newsletter.objects.order_by('-publication')
    #posts = Newsletter.objects
    return render(request, 'allposts.html', {"posts": posts})

def render_to_response(param):
    pass

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


