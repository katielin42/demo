from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .models import Blog
# Create your views here.


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'allblogs.html', {"blogs": blogs})

def render_to_response(param):
    pass


def detail(request, blog_id):
    
    detail_blog = get_object_or_404(Blog,pk=blog_id)
    if detail_blog== Http404:
        print("error msg")
        return render(request, 'blog/error.html')
    print("here")

    try:
        detail_blog = Blog.objects.get(pk=blog_id)
        return render(request, 'detail.html', {"blog": detail_blog})
    except Blog.DoesNotExist:
        return render(request, 'error.html')
