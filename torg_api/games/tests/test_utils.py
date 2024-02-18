import pytest
from typing import Union
from players.models import Player
from ..utils import get_winner


class TestGetWinner:

    @pytest.fixture
    def player_1(self, player_factory):
        player_1 = player_factory(name="Test_player_1")
        return player_1

    @pytest.fixture
    def player_2(self, player_factory):
        player_2 = player_factory(name="Test_player_2")
        return player_2

    @pytest.mark.parametrize("player_1, player_2, score_1, score_2, result", (
            (player_1, player_2, 3, 2, player_1),
            (player_1, player_2, 2, 3, player_2),
            (player_1, player_2, 2, 2, None),
    ))
    def test_get_winner(self, player_1: type[Player], player_2: type[Player], score_1: int, score_2: int, result) -> \
            Union[type[Player], None]:
        assert get_winner(player_1, player_2, score_1, score_2) == result
