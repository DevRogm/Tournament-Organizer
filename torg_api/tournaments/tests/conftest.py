from pytest_factoryboy import register
from .factories import TournamentFactory, UserFactory
from players.tests.factories import PlayerFactory

register(TournamentFactory)
register(UserFactory)
register(PlayerFactory)
