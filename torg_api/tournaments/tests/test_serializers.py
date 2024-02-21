from collections import OrderedDict
import json
import pytest
from django.contrib.auth.models import User
from tournaments.serializers import TournamentSerializer, UsersSerializer
from players.serializers import PlayerSerializer
from players.tests import factories, conftest
from players.models import Player
from rest_framework import serializers

pytestmark = pytest.mark.django_db


class TestUserSerializer:
    expected_data = {'username': 'test_user', 'email': 'test@user.pl'}

    @pytest.fixture
    def user(self, user_factory):
        user = user_factory(username=self.expected_data['username'], email=self.expected_data['email'])
        return user

    def test_user_data(self, user):
        serializer = UsersSerializer(instance=user)
        assert serializer.data == self.expected_data


class TestTournamentSerializer:
    username = 'tester'
    expected_data = {"id": 1, "name": "test_name", "num_of_players": 4, "description": "Test tournament description",
                     "organizer": {"username": "tester", "email": "test@user.pl"}, "tournament_status": "waiting",
                     "players": []}

    @pytest.fixture
    def tournament(self, tournament_factory):
        tournament = tournament_factory(name="test_name")
        tournament.organizer.username = self.username
        return tournament

    @pytest.fixture
    def players(self, player_factory):
        players = [player_factory() for _ in range(1, 40)]
        return players

    def test_tournament_simple_data(self, tournament):
        serializer = TournamentSerializer(instance=tournament)
        assert serializer.data == self.expected_data
        assert not self.expected_data['players']

    def test_tournament_data_add_players(self, tournament, players):
        [tournament.players.add(player) for player in players[:4]]
        tournament_serializer = TournamentSerializer(instance=tournament)
        assert tournament_serializer['players']

    def test_tournament_data_with_add_too_much_players_using_api(self, tournament, players):
        tournament_serializer = TournamentSerializer(instance=tournament)
        with pytest.raises(serializers.ValidationError):
            [tournament.players.add(player) for player in players[:6]]
            tournament_serializer.validators[0](tournament_serializer.data)
