import random
from typing import List, Union


def is_even(number: int) -> bool:
    """
    Function that checks if number is even or not
    :param number: number to check
    :return: true or false
    """
    return True if number % 2 == 0 else False


def is_half_of_previous_rounds(length_of_previous_round: Union[int, None], length_current_round: int) -> bool:
    """
    Function that checks whether the length of current rounds is half the length of previous rounds
    :param length_of_previous_round: Number of games in the previous round
    :param length_current_round: Number of games in the current round
    :return: true of false
    """
    if not length_of_previous_round:
        return True
    elif length_of_previous_round / length_current_round == 2:
        return True
    else:
        return False


def generate_games(num_of_players: int, tournament_name: str, tournament_players_list: list) -> List[dict]:
    """
    Function that generates games depends on num of players and draws pairs for the first round
    Number of games is always one less than the number of players
    Number of games per round is always half the previous number of games
    """
    list_of_games = []
    games_in_round = None
    count = 1
    length_of_previous_round = None

    # iterating through the number of players down by one
    for number in range(num_of_players, 1, -1):
        games_in_round = number // 2
        if is_even(games_in_round) and is_half_of_previous_rounds(length_of_previous_round, games_in_round):
            for column in range(1, int(games_in_round) + 1):
                if count == 1:
                    random.shuffle(tournament_players_list)
                    player_1 = tournament_players_list.pop()
                    player_2 = tournament_players_list.pop()
                else:
                    player_1 = None
                    player_2 = None
                list_of_games.append(
                    {"name": f"{tournament_name}_game_{count}_{column}", "game_round": count, "game_num": column,
                     "player_1": player_1,
                     "player_2": player_2})
            count += 1
            length_of_previous_round = games_in_round
    # if games in round is one then this is a final round
    if games_in_round == 1:
        list_of_games.append({"name": f"{tournament_name}_game_{count}_{1}", "game_round": count, "game_num": 1})
    return list_of_games
