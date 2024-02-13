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


def generate_games(num_of_players, tournament_name):
    """
    Function that generate games depends on num of players
    """
    list_of_games = []
    games_in_round = None
    count = 1
    length_of_previous_round = None
    for number in range(num_of_players, 1, -1):
        games_in_round = int(number / 2)
        if is_even(games_in_round) and is_half_of_previous_rounds(length_of_previous_round, games_in_round):
            for column in range(1, int(games_in_round) + 1):
                list_of_games.append({"name": f"{tournament_name}_game_{count}_{column}", "round": count})
            count += 1
            length_of_previous_round = games_in_round

    if games_in_round == 1:
        list_of_games.append({"name": f"{tournament_name}_game_{count}_{1}", "round": count})
    return list_of_games
