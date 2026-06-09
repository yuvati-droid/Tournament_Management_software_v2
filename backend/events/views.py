from rest_framework import viewsets
from .models import Event
from .serializer import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.permissions import IsAdmin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event
from .serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):

        event = self.get_object()

        event.status = 'PUBLISHED'
        event.save()

        return Response(
            {
                "message": "Event published successfully",
                "status": event.status
            },
            status=status.HTTP_200_OK
        )

class EventCreateView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        return Response({"message": "Allowed"})
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

