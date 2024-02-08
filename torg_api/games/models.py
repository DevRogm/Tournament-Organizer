from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=30, default='')
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.PROTECT)
    player_1 = models.ForeignKey('players.Player', on_delete=models.PROTECT, related_name='player_1')
    player_2 = models.ForeignKey('players.Player', on_delete=models.PROTECT, related_name='player_2')
