from django.db import models

# Create your models here.
class Team(models.Model):
    profile_pic = models.ImageField(upload_to='picx', default = "EELogo_Temp.png")
    name = models.CharField(max_length=240)
    title = models.TextField()
    email = models.TextField()


    def __str__(self): # displays actual title on admin page
        return self.title
