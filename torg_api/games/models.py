from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=30, default='')
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.PROTECT, related_name='games')
    player_1 = models.ForeignKey('players.Player', on_delete=models.PROTECT, related_name='player_1', null=True,
                                 blank=True)
    player_2 = models.ForeignKey('players.Player', on_delete=models.PROTECT, related_name='player_2', null=True,
                                 blank=True)
    score_1 = models.PositiveIntegerField(null=True, default=None, blank=True)
    score_2 = models.PositiveIntegerField(null=True, default=None, blank=True)
    winner = models.CharField(max_length=30, null=True, default=None, blank=True)
    round = models.PositiveIntegerField(null=True, default=None, blank=True)
