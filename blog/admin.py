from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Blog


admin.site.register(Blog)
