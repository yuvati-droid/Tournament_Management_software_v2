from rest_framework import viewsets
from .models import VenueGround
from .serializer import VenueGroundSerializer


class VenueGroundViewSet(viewsets.ModelViewSet):
    queryset = VenueGround.objects.all()
    serializer_class = VenueGroundSerializer