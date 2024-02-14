from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game
from tournaments.serializers import TournamentSerializer
from players.serializers import PlayerSerializer
from .validators import GameResultApproveValidator


class GameSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(read_only=True)
    player_1 = PlayerSerializer(read_only=True)
    player_2 = PlayerSerializer(read_only=True)
    validators = [GameResultApproveValidator()]

    class Meta:
        model = Game
        fields = ('id', 'name', 'tournament', 'player_1', 'player_2', 'score_1', 'score_2', 'winner', 'is_approved')
        extra_kwargs = {
            'winner': {'read_only': True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=['name', 'tournament']
            )
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('tournament')
        return representation
