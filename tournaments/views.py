from rest_framework import viewsets
from .models import Tournament
from .serializer import TournamentSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer