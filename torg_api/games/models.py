from django.db import models
from django.core.validators import MaxValueValidator

class Game(models.Model):
    name = models.CharField(max_length=30, default='')
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.PROTECT, related_name='games')
    player_1 = models.ForeignKey('players.Player', on_delete=models.PROTECT, related_name='player_1', null=True,
                                 blank=True)
    player_2 = models.ForeignKey('players.Player', on_delete=models.PROTECT, related_name='player_2', null=True,
                                 blank=True)
    score_1 = models.PositiveIntegerField(null=True, default=None, blank=True, validators=[MaxValueValidator(1000)])
    score_2 = models.PositiveIntegerField(null=True, default=None, blank=True, validators=[MaxValueValidator(1000)])
    game_round = models.PositiveIntegerField(null=True, default=None, blank=True, validators=[MaxValueValidator(5)])
    game_num = models.PositiveIntegerField(null=True, default=None, blank=True, validators=[MaxValueValidator(16)])
    is_approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ['name', 'tournament']