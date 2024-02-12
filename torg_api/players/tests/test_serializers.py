# def test_tournament_data_add_players(self, tournament, players):
#     [tournament.players.add(player) for player in players[:4]]
#     tournament_serializer = TournamentSerializer(instance=tournament)
#     self.expected_data['players'] = tournament_serializer.data['players']
#     assert len(self.expected_data['players']) == 4
#     assert list(self.expected_data['players'][0].keys()) == ['id', 'name']