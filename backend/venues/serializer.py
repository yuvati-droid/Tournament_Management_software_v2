from rest_framework import serializers
from .models import Venue
from venue_grounds.models import VenueGround

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class VenueGroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueGround
        fields = '__all__'