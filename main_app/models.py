from django.db import models
from django.urls import reverse

# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=100)
    scientific = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bug_id': self.id})