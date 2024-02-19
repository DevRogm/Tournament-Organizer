from pytest_factoryboy import register
from .factories import GameFactory
from players.tests.factories import PlayerFactory

register(GameFactory)
register(PlayerFactory)
