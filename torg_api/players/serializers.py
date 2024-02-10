from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name',)
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        player, created = Player.objects.get_or_create(name=validated_data['name'],
                                                       organizer=validated_data['organizer'])
        return player
