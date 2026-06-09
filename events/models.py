from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    banner_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    guidelines = models.TextField(blank=True, null=True)

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name