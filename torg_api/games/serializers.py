from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game
from tournaments.serializers import TournamentSerializer
from players.serializers import PlayerSerializer


class GameSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    player_1 = PlayerSerializer(read_only=True)
    player_2 = PlayerSerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'tournament', 'player_1', 'player_2', 'score_1', 'score_2', 'winner')
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=['name', 'tournament']
            )
        ]
