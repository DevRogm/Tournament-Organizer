from rest_framework import serializers
from .models import Player
from tournaments.serializers import TournamentSerializer, UserSerializer


class PlayerSerializer(serializers.ModelSerializer):
    tournament = TournamentSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Player
        fields = ('name', 'tournament')
