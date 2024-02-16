import pytest
import json

pytestmark = pytest.mark.django_db


class TestPlayerEndpoints:
    endpoint = "/api/players/"

    @pytest.fixture
    def player(self, player_factory):
        player = player_factory(name="Test_player_name")
        return player

    def test_players_get_if_not_auth(self, player, api_client):
        response = api_client().get(self.endpoint)
        assert response.status_code == 403

    def test_players_get_if_auth(self, player, logged_user):
        logged_user.force_login(player.organizer)
        response = logged_user.get(self.endpoint)
        assert response.status_code == 200

    def test_players_get_data_with_one_player(self, player, logged_user):
        logged_user.force_login(player.organizer)
        response = logged_user.get(self.endpoint)
        assert response.status_code == 200
        assert ('id', 'name') == tuple(json.loads(response.content)[0].keys())

    def test_players_get_data_with_many_players(self, player, player_factory, logged_user):
        players = player_factory.create_batch(3, organizer=player.organizer)
        logged_user.force_login(players[0].organizer)
        response = logged_user.get(self.endpoint)
        assert ('id', 'name') == tuple(json.loads(response.content)[0].keys())
        assert len(json.loads(response.content)) == 4

