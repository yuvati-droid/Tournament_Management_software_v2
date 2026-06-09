from django.db import models
from django.db import models


class Sport(models.Model):

    SCORING_TYPES = (
        ('POINTS', 'Points'),
        ('RUNS', 'Runs'),
        ('GOALS', 'Goals'),
        ('SETS', 'Sets'),
        ('CUSTOM', 'Custom'),
    )

    name = models.CharField(max_length=100, unique=True)

    scoring_type = models.CharField(
        max_length=20,
        choices=SCORING_TYPES
    )

    tiebreak_config = models.JSONField(
        default=dict,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
