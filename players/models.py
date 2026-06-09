from django.db import models
from django.contrib import admin
# Create your models here.
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name