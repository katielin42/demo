from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Newsletter


admin.site.register(Newsletter)
