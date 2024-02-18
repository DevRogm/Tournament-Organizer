import random
from typing import List, Union


def is_even(number: float) -> bool:
    """
    Function that checks if number is even or not
    :param number: number to check
    :return: true or false
    """
    return True if number % 2 == 0 else False


def is_half_of_previous_rounds(length_of_previous_round: Union[float, None], length_current_round: float) -> bool:
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
    :param num_of_players:
    :param tournament_name:
    :param tournament_players_list:
    :return:
    Example:
    If the number of players is up to 32, the total number of generated games will be 31
    according to the equation number_of_all_games = number_of_players - 1
    Number of rounds depending on the number of players:
    2 -> 1
    4 -> 2
    8 -> 3
    16 -> 4
    32 -> 5
    """

    list_of_games = []
    games_in_round = None
    game_round = 1
    length_of_previous_round = None

    # iterating through the number of players down by one
    for number in range(num_of_players, 1, -1):
        games_in_round = number / 2
        # If games_in_round is even and this number is half of the previous number of games in the round, then this is
        # appropriate number of games to create a new round, if there was no first round then the first round is created
        if is_even(games_in_round) and is_half_of_previous_rounds(length_of_previous_round, games_in_round):
            for game_num in range(1, int(games_in_round) + 1):
                # If we generate games for the first round, draw pairs of players
                # otherwise assign none
                if game_round == 1:
                    random.shuffle(tournament_players_list)
                    player_1 = tournament_players_list.pop()
                    player_2 = tournament_players_list.pop()
                else:
                    player_1 = None
                    player_2 = None
                # Create a list of games with names suggesting the round number and game number,
                # and players assigned or not
                list_of_games.append(
                    {"name": f"{tournament_name}_game_{game_round}_{game_num}", "game_round": game_round,
                     "game_num": game_num,
                     "player_1": player_1,
                     "player_2": player_2})
            game_round += 1
            length_of_previous_round = games_in_round
    # if games in round is one then this is a final round
    if games_in_round == 1:
        list_of_games.append(
            {"name": f"{tournament_name}_game_{game_round}_{1}", "game_round": game_round, "game_num": 1})
    return list_of_games
