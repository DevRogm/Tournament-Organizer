from .models import Tournament
from .serializers import TournamentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


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
