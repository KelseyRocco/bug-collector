from django.db import models

# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=100)
    scientific = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)

