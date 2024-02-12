from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class NumOfPlayersValidator:

    def __init__(self, num_of_players="num_of_players", players="players"):
        self.num_of_players = num_of_players
        self.players = players

    def __call__(self, attrs):
        if attrs[self.num_of_players] < len(attrs[self.players]):
            message = f"Number of players cannot be more than {attrs[self.num_of_players]}"
            raise serializers.ValidationError({'players': _(message)})


class TournamentStatusValidator():

    def __init__(self, num_of_players="num_of_players", players="players", tournament_status="tournament_status"):
        self.num_of_players = num_of_players
        self.players = players
        self.tournament_status = tournament_status

    def __call__(self, attrs):
        if (attrs[self.num_of_players] != len(attrs[self.players])) and attrs[self.tournament_status] == "ongoing":
            message = (f"If you want to start the tournament, the number of added players should be "
                       f"{attrs[self.num_of_players]}")
            raise serializers.ValidationError({'tournament_status': _(message)})
