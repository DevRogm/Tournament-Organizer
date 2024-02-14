from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game
from .utils import get_winner, get_next_game


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
        if serializer.validated_data['is_approved'] and not self.get_object().is_approved:
            winner_obj = get_winner(game.player_1, game.player_2, game.score_1, game.score_2)
            if winner_obj:
                next_game_round, next_game_num = get_next_game(game.game_round, game.game_num)
                next_game = Game.objects.get(tournament=game.tournament, game_round=next_game_round,
                                             game_num=next_game_num)
                if not next_game.player_1:
                    next_game.player_1 = winner_obj
                elif not next_game.player_2 and next_game.player_1 != winner_obj:
                    next_game.player_2 = winner_obj
                next_game.save()
        serializer.save()
