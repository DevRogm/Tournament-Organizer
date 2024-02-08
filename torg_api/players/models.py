from django.db import models
from tournaments.models import Tournament


class Player(models.Model):
    name = models.CharField(max_length=30, unique=True)
    tournament = models.ManyToManyField(Tournament, related_name='players')

    def __str__(self):
        return self.name

