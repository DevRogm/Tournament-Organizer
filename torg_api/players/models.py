from django.db import models
from django.conf import settings


class Player(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, unique=True)
    tournament = models.ManyToManyField('tournaments.Tournament', related_name='players',
                                        blank=True)

    class Meta:
        unique_together = ["organizer", "name"]

    def __str__(self):
        return self.name
