from django import views
from django.urls import path
#import newsletter.views
import newsletter.views
urlpatterns = [
    path('', newsletter.views.allposts, name='allposts'),
    path('<int:post_id>/', newsletter.views.detail, name= 'detail'),
]