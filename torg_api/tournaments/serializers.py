from .models import Tournament
from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User
from players.serializers import PlayerSerializer
from players.models import Player
from .validators import NumOfPlayersValidator, TournamentStatusValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TournamentSerializer(serializers.ModelSerializer):
    """
    Serializer for tournament model with validator.
    Validators check whether the appropriate number of players is not greater than the maximum and whether the
    tournament status can be changed
    """
    players = PlayerSerializer(many=True, required=False)
    organizer = UserSerializer(read_only=True)
    requires_context = True
    validators = [NumOfPlayersValidator(), TournamentStatusValidator()]

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'num_of_players', 'description', 'organizer', 'tournament_status', 'players')
        read_only_fields = ('organizer',)

    def update(self, instance, validated_data):
        """
        Modified function to allow adding nested fields as players
        """
        players_data = validated_data.pop("players")
        instance.players.set([])
        if players_data:
            [instance.players.add(Player.objects.get(**player)) for player in players_data]
        super().update(instance=instance, validated_data=validated_data)
        return instance
