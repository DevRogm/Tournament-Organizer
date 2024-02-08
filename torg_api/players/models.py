from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=30, unique=True)
    tournament = models.ManyToManyField('tournaments.Tournament', related_name='players')

    def __str__(self):
        return self.name
