from rest_framework import viewsets
from .models import Sport
from .serializer import SportSerializer

class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer