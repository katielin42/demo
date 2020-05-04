from django.db import models

# Create your models here.
class Newsletter(models.Model):
    title = models.CharField(max_length=240)
    publication = models.DateTimeField()
    body = models.TextField()

    def __str__(self): # displays actual title on admin page
        return self.title

    '''
        def summary(self):
            return self.body[:300]
    '''