from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=150)
