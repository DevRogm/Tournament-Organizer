from .models import Tournament
from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class TournamentSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)

    class Meta:
        model = Tournament
        fields = ('name', 'num_of_players', 'description', 'organizer')
        read_only_fields = ('organizer',)
