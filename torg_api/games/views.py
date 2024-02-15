import datetime

from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game
from .utils import get_winner, get_next_game


class GameListView(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Game.objects.filter(tournament__organizer=self.request.user).select_related("tournament__organizer")
        return queryset


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Game.objects.filter(tournament__organizer=self.request.user).select_related("tournament__organizer")
        return queryset

    def perform_update(self, serializer):
        game = self.get_object()
        if serializer.validated_data['is_approved'] and not game.is_approved:
            winner_obj = get_winner(game.player_1, game.player_2, game.score_1, game.score_2)
            next_game = get_next_game(game.game_round, game.game_num, game.tournament)
            if winner_obj and next_game:
                if not next_game.player_1:
                    next_game.player_1 = winner_obj
                elif not next_game.player_2 and next_game.player_1 != winner_obj:
                    next_game.player_2 = winner_obj
                next_game.save()
            if not next_game:
                tournament = game.tournament
                tournament.tournament_status = 'complete'
                tournament.end_date = datetime.datetime.now()
                tournament.save()
        serializer.save()
