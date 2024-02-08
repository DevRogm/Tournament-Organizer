import pytest

pytestmark = pytest.mark.django_db


class TestPlayerModel:
    test_player_name = "Test_player_name"

    @pytest.fixture
    def player(self, player_factory):
        player = player_factory(name="Test_player_name")
        return player

    def test_player_str(self, player):
        assert player.__str__() == self.test_player_name
