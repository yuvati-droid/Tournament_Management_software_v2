from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Venue
from venue_grounds.models import VenueGround
from .serializer import VenueSerializer, VenueGroundSerializer


class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


@api_view(['POST'])
def add_ground(request, id):
    try:
        venue = Venue.objects.get(id=id)
    except Venue.DoesNotExist:
        return Response(
            {"error": "Venue not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    data = request.data.copy()
    data['venue'] = venue.id

    serializer = VenueGroundSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )