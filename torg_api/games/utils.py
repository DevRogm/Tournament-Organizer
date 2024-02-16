from ..tournaments.utils import is_even
from .models import Game
from django.core.exceptions import ObjectDoesNotExist
from ..players.models import Player
from ..tournaments.models import Tournament
from typing import Union


def get_winner(player_1: type[Player], player_2: type[Player], score_1: int, score_2: int) -> Union[type[Player], None]:
    """
    The function returns a Player object for the player who wins the match or None in case of a tie.
    The winner is selected based on score_1 and score_2.

    :param player_1: Player 1 instance
    :param player_2: Player 2 instance
    :param score_1: Player 1 score
    :param score_2: Player 2 score
    :return: None or Player object
    """
    if score_1 > score_2:
        return player_1
    elif score_1 < score_2:
        return player_2
    else:
        return None


def get_next_game(game_round: int, game_num: int, tournament: type[Tournament]) -> Union[type[Game], None]:
    """
    The function checks whether a next game exists and returns a Game object for the next game. If not, returns None.
    To check whether there is another game, you need the next round number and the next game number.
    :param game_round: Current game round
    :param game_num: Current game number
    :param tournament: Tournament object
    :return: Game object for next game or None
    """
    # If the current game number is 1 or 2, the next game should be number 1,
    # if 3 or 4, it should be number 2 and so on.
    if is_even(game_num):
        next_game_num = game_num // 2
    else:
        next_game_num = (game_num + 1) // 2
    next_game_round = game_round + 1
    # Check if there is a next game
    try:
        next_game = Game.objects.get(tournament=tournament, game_round=next_game_round,
                                     game_num=next_game_num)
    except ObjectDoesNotExist:
        return None
    return next_game
