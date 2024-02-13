from .serializers import GameSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Game


class GameListView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


class GameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]


    def perform_update(self, serializer):
        if serializer.validated_data['score_1'] and serializer.validated_data['score_2']:
            print("Jak tak to mozna zatwierdzic wynik meczu i jesli zostanie zatwierdzone czyli is_approve = True to wtedy wywolujemy funkcje przeniesienia gracza do kolejnej rundy do odpowiedniego meczu")
        # if serializer.validated_data['tournament_status'] == 'ongoing':
        #     game_list = generate_games(tournament.num_of_players, tournament.name, list(tournament.players.all()))
        #     if game_list and not tournament.games.all():
        #         games_obj_to_create = [Game(tournament=tournament, **game_data) for game_data in game_list]
        #         Game.objects.bulk_create(games_obj_to_create)
        serializer.save()