from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'tournament', 'player_1', 'score_1', 'player_2', 'score_2', 'winner', 'round')
