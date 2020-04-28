from django.contrib import admin

# Register your models here.
from .models import Job

admin.site.register(Job)
# what to show up in admin page