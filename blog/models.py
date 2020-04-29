from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=240)
    publication = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def __str_(self):
        return self.title
