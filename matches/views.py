from rest_framework import viewsets
from .models import Match
from .serializer import MatchSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
