from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=240)
    title = models.TextField()
    description = models.TextField()

    def __str__(self): # displays actual title on admin page
        return self.title
