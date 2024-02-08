import pytest

pytestmark = pytest.mark.django_db


class TestGameModel:
    @pytest.fixture
    def game(self, game_factory):
        game = game_factory()
        return game

    def test_game_init(self, game):
        assert game


