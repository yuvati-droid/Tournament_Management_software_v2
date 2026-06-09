from django.db import models
from django.contrib import admin
# Create your models here.
from django.db import models
from events.models import Event

class Team(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='teams'
    )

    name = models.CharField(max_length=255)

    logo_url = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name