from django.db import models
from django.db import models 
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    date = models.DateField()
    artist_name = models.CharField(max_length=60)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}, {self.date}, {self.location}"
