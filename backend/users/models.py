from django.db import models
from django.utils import timezone

class User(models.Model):

    ROLE_CHOICES = (
        ('SUPER_ADMIN', 'Super Admin'),
        ('ADMIN', 'Admin'),
        ('TEAM_OWNER', 'Team Owner'),
        ('SCORER', 'Scorer'),
        ('COMMENTATOR', 'Commentator'),
        ('VIEWER', 'Viewer'),
        ('BROADCAST_MANAGER', 'Broadcast Manager'),
    )

    username = models.CharField(max_length=100, default='tempuser')

    email = models.EmailField(
        unique=True,
        default='default@example.com'
    )

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='VIEWER'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.username