from rest_framework import serializers
from .models import Venue, VenueGround


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'