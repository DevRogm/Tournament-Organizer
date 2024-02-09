from .models import Player
from rest_framework import generics
from .serializer import PlayersSerializer
from rest_framework.permissions import IsAuthenticated
from tournaments.models import Tournament


class PlayersListView(generics.ListCreateAPIView):
    serializer_class = PlayersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Player.objects.filter(organizer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
