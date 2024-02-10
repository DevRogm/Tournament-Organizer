from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game


class GameListView(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Game.objects.filter(organizer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Game.objects.filter(organizer=self.request.user)
        return queryset
