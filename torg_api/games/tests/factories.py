from games.models import Game
from players.tests.factories import PlayerFactory
from tournaments.tests.factories import TournamentFactory
import factory


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Sequence(lambda n: f"Test_game_name_{n}")
    tournament = factory.SubFactory(TournamentFactory)
    player_1 = factory.SubFactory(PlayerFactory)
    player_2 = factory.SubFactory(PlayerFactory)
