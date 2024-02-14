from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game
from .utils import get_winner, move_winner

class GameListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        game = self.get_object()

        if serializer.validated_data['is_approved'] and not self.get_object().winner:
            winner_obj = get_winner(game.player_1, game.player_2, game.score_1, game.score_2)
            print(winner_obj)
            if winner_obj:
                # move_winner()
                print("Push winner to the next round")
        serializer.save()
