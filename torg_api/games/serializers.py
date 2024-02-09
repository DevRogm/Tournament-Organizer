from rest_framework import serializers
from .models import Game
from tournaments.serializers import TournamentSerializer
from players.serializers import PlayerSerializer


class GameSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(required=True)
    player_1 = PlayerSerializer(required=False)
    player_2 = PlayerSerializer(required=False)

    class Meta:
        model = Game
        fields = ('name', 'tournament', 'player_1', 'player_2', 'score_1', 'score_2', 'winner')
