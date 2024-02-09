from pytest_factoryboy import register
from .factories import TournamentFactory, UserFactory

register(TournamentFactory)
register(UserFactory)
