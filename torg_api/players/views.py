from .models import Player
from rest_framework import generics
from .serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated


class PlayersListView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]  # need to add custom permission

    def get_queryset(self):
        queryset = Player.objects.filter(organizer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class PlayerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Player.objects.filter(organizer=self.request.user)
        return queryset