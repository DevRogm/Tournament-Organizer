from tournaments.utils import is_even


def get_winner(player_1, player_2, score_1, score_2):
    if score_1 > score_2:
        return player_1
    elif score_1 < score_2:
        return player_2
    else:
        return None


def get_next_game(game_round, game_num):
    if is_even(game_num):
        next_game_num = game_num // 2
    else:
        next_game_num = (game_num + 1) // 2
    next_game_round = game_round + 1
    return next_game_round, next_game_num
