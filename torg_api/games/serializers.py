from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Game
from players.serializers import PlayerSerializer
from .validators import GameResultApproveValidator


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for game model with validator. The validator checks whether the game result can be confirmed.
    """
    player_1 = PlayerSerializer(read_only=True)
    player_2 = PlayerSerializer(read_only=True)
    validators = [GameResultApproveValidator()]

    class Meta:
        model = Game
        fields = (
            'id', 'name', 'player_1', 'player_2', 'score_1', 'score_2', 'is_approved', 'game_round',
            'game_num')
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=['name', 'tournament']
            )
        ]
