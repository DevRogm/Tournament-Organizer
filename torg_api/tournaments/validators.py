from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class NumOfPlayersValidator:
    """
    The validator checks whether the appropriate number of players is not greater than the maximum
    """

    def __init__(self, num_of_players="num_of_players", players="players"):
        self.num_of_players = num_of_players
        self.players = players

    def __call__(self, attrs: dict) -> None:
        """
        This method checks whether the number of entered players is not greater than the maximum number of players
        in the tournament. Otherwise we will receive ValidationError
        :param attrs: dictionary with tournament attributes and their values
        :return: None
        """
        if attrs[self.num_of_players] < len(attrs[self.players]):
            message = f"Number of players cannot be more than {attrs[self.num_of_players]}"
            raise serializers.ValidationError({'players': _(message)})


class TournamentStatusValidator:
    """
    The validator checks whether the tournament can be started
    """

    def __init__(self, num_of_players="num_of_players", players="players", tournament_status="tournament_status"):
        self.num_of_players = num_of_players
        self.players = players
        self.tournament_status = tournament_status

    def __call__(self, attrs: dict) -> None:
        """
        When trying to change the tournament status to 'ongoing', the method will check whether the number of players
        provided is different from the required number of players. If so, we will receive ValidationError
        :param attrs:
        :return: None
        """
        if (attrs[self.num_of_players] != len(attrs[self.players])) and attrs[self.tournament_status] == "ongoing":
            message = (f"If you want to start the tournament, the number of added players should be "
                       f"{attrs[self.num_of_players]}")
            raise serializers.ValidationError({'tournament_status': _(message)})
