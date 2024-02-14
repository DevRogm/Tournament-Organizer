from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game


class GameListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.validated_data['is_approved'] and not self.get_object().winner:
            print("Assign winner")
            print("Push winner to the next round")
        serializer.save()
