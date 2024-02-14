from tournaments.utils import is_even
from .models import Game
from django.core.exceptions import ObjectDoesNotExist
def get_winner(player_1, player_2, score_1, score_2):
    if score_1 > score_2:
        return player_1
    elif score_1 < score_2:
        return player_2
    else:
        return None


def get_next_game(game_round, game_num, tournament):
    if is_even(game_num):
        next_game_num = game_num // 2
    else:
        next_game_num = (game_num + 1) // 2
    next_game_round = game_round + 1
    try:
        next_game = Game.objects.get(tournament=tournament, game_round=next_game_round,
                                 game_num=next_game_num)
    except ObjectDoesNotExist:
        next_game = None
    return next_game
