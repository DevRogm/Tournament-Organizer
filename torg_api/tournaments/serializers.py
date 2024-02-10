from .models import Tournament
from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User
from players.serializers import PlayerSerializer
from players.models import Player


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TournamentSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, required=False)
    organizer = UserSerializer(read_only=True)
    requires_context = True

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'num_of_players', 'description', 'organizer', 'tournament_status', 'players')
        read_only_fields = ('organizer',)

    def update(self, instance, validated_data):
        players_data = validated_data.pop("players")
        if players_data:
            if len(players_data) > instance.num_of_players:
                raise serializers.ValidationError(
                    f'The number of players should not be more than {instance.num_of_players}')
            instance.players.set([])
            [instance.players.add(Player.objects.get(**player)) for player in players_data]
        else:
            instance.players.set([])
        return instance
