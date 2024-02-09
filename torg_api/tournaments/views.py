from django.shortcuts import render
from .models import Tournament
from .serializers import TournamentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class TournamentListView(generics.ListCreateAPIView):
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tournament.objects.filter(organizer=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
