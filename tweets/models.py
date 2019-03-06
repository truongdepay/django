from django.db import models

# Create your models here.

class Tweet(models.Model):

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.title)

