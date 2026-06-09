from django.db import models

class VenueGround(models.Model):
    venue = models.ForeignKey(
        'venues.Venue',
        on_delete=models.CASCADE,
        related_name='grounds'
    )
    ground_name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.ground_name