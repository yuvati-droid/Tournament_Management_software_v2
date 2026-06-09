from django.db import models

# Create your models here.
from django.db import models
from events.models import Event
from sports.models import Sport

class Tournament(models.Model):

    FORMAT_CHOICES = [
        ('knockout', 'Knockout'),
        ('league', 'League'),
        ('round_robin', 'Round Robin'),
        ('playoffs', 'Playoffs'),
    ]

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)

    format = models.CharField(
        max_length=30,
        choices=FORMAT_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming'
    )

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name