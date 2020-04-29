
from django.urls import path
import blog.views
urlpatterns = [
    path('', blog.views.allblogs, name='allblogs'),
    path('<int:blog_id>/',blog.views.detail, name= 'detail'), # if you find an int after blog/ go to views.detail
]