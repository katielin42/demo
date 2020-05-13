"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import portfolio.views
from portfolio import views
import newsletter.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('team/', include('ourTeam.urls')),
    # path('blog/', include('blog.urls')), # groups all urls with newsletter/ to be sent to the blog app
    path('newsletter/', include('newsletter.urls')),
    path('events/', views.events, name = 'events'),
    path('club/', views.club, name='club'),
    path('search/', newsletter.views.filteredposts, name = 'search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
