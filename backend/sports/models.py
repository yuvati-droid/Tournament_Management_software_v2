from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
class Sport(models.Model):
    SCORING_TYPES = [
        ('ball_by_ball', 'Ball By Ball'),
        ('game_set_point', 'Game Set Point'),
    ]

    name = models.CharField(max_length=100)

    scoring_type = models.CharField(
        max_length=50,
        choices=SCORING_TYPES
    )

    max_players = models.IntegerField(default=0)

    reserve_players = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name