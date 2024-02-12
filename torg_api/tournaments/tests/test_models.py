import pytest

pytestmark = pytest.mark.django_db


class TestTournamentModel:
    @pytest.fixture
    def tournament(self, tournament_factory):
        tournament = tournament_factory(name="test_name")
        return tournament

    def test_tournament_str(self, tournament):
        assert tournament.__str__() == "test_name"
