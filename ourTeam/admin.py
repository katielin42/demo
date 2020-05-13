from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Team


admin.site.register(Team)