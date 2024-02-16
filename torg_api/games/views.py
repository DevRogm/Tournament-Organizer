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
        queryset = Game.objects.filter(tournament__organizer=self.request.user).select_related(
            "tournament__organizer", "player_1", "player_2").prefetch_related("tournament__players")
        return queryset


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Game.objects.filter(tournament__organizer=self.request.user).select_related(
            "tournament__organizer", "player_1", "player_2").prefetch_related("tournament__players")
        return queryset

    def perform_update(self, serializer):
        game = self.get_object()
        if serializer.validated_data['is_approved'] and not game.is_approved:
            # Find the winner
            winner_obj = get_winner(game.player_1, game.player_2, game.score_1, game.score_2)
            # Check if there is another game
            next_game = get_next_game(game.game_round, game.game_num, game.tournament)
            # If there is a winner and there is another game, put the winner in it
            if winner_obj and next_game:
                if not next_game.player_1:
                    next_game.player_1 = winner_obj
                elif not next_game.player_2 and next_game.player_1 != winner_obj:
                    next_game.player_2 = winner_obj
                next_game.save()
            # If there is no next game, it means that it was the final and the tournament can be ended
            if not next_game:
                tournament = game.tournament
                tournament.tournament_status = 'complete'
                tournament.end_date = datetime.datetime.now()
                tournament.save()
        serializer.save()
