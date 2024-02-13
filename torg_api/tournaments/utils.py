import random


def is_even(number):
    """
    Function that checks if number is even or not
    """
    return True if number % 2 == 0 else False


def is_half_of_previous_rounds(length_of_previous_round, length_current_round):
    """
    Function that checks whether the number of current rounds is half the number of previous rounds
    """
    if not length_of_previous_round:
        return True
    elif length_of_previous_round / length_current_round == 2:
        return True
    else:
        return False


def generate_games(num_of_players, tournament_name, tournament_players_list):
    """
    Function that generates games depends on num of players and draws pairs for tge first round
    """
    list_of_games = []
    games_in_round = None
    count = 1
    length_of_previous_round = None
    player_1 = ""
    player_2 = ""
    for number in range(num_of_players, 1, -1):
        games_in_round = int(number / 2)
        if is_even(games_in_round) and is_half_of_previous_rounds(length_of_previous_round, games_in_round):
            for column in range(1, int(games_in_round) + 1):
                if count == 1:
                    random.shuffle(tournament_players_list)
                    player_1 = tournament_players_list.pop()
                    player_2 = tournament_players_list.pop()
                list_of_games.append(
                    {"name": f"{tournament_name}_game_{count}_{column}", "round": count, "player_1": player_1,
                     "player_2": player_2})
            count += 1
            length_of_previous_round = games_in_round

    if games_in_round == 1:
        list_of_games.append({"name": f"{tournament_name}_game_{count}_{1}", "round": count})
    return list_of_games
