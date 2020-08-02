from django.db import models

# Create your models here.
class Team(models.Model):
    profile_pic = models.ImageField(upload_to='picx', default = "EELogo_Temp.png")
    name = models.CharField(max_length=240)
    position = models.CharField(max_length=240, default = "Something Rep.")# crop to fit the club.html cards
    icon = models.CharField(max_length=240, default = "fa fa-icon")
    description_1 = models.TextField(default="Shall be responsible for ...")
    description_2 = models.TextField(default="Shall be responsible for ...")
    description_3 = models.TextField(default="Shall be responsible for ...")
    description_4 = models.TextField(default="Shall be responsible for ...")
    description_5 = models.TextField(default="Shall be responsible for ...")
    email = models.EmailField()
    isSenior = models.BooleanField(default=False)
    isDuplicateDescription=models.BooleanField(default=False)
    isFilled = models.BooleanField(default=True)



    def __str__(self): # displays actual title on admin page
        return self.position
  