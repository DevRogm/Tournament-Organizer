from .models import Tournament
from games.models import Game
from .serializers import TournamentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from .utils import generate_games


class TournamentListView(generics.ListCreateAPIView):
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'num_of_players', 'tournament_status']
    ordering_fields = ['name', 'num_of_players', 'tournament_status']

    def get_queryset(self):
        queryset = Tournament.objects.filter(organizer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class TournamentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tournament.objects.filter(organizer=self.request.user)
        return queryset

    def perform_update(self, serializer):
        tournament = Tournament.objects.get(name=serializer.validated_data['name'])
        if serializer.validated_data['tournament_status'] == 'ongoing':
            game_list = generate_games(tournament.num_of_players, tournament.name)
            if game_list:
                games_obj_to_create = [Game(tournament=tournament, **game_data) for game_data in game_list]
                Game.objects.bulk_create(games_obj_to_create)
        serializer.save()
