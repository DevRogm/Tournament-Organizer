from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

class Tournament(models.Model):
    PLAYERS_NUM = [(2 ** num, 2 ** num) for num in range(1, 6)]
    STATUS_CHOICES = (
        ('waiting', 'Waiting'),
        ('ongoing', 'Ongoing'),
        ('complete', 'Complete')
    )

    name = models.CharField(max_length=30, unique=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    num_of_players = models.IntegerField(choices=PLAYERS_NUM, default=2)
    players = models.ManyToManyField('players.Player', blank=True, related_name='tournament')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(default=None, null=True, blank=True)
    end_date = models.DateTimeField(default=None, null=True, blank=True)
    tournament_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

    def __str__(self):
        return self.name

