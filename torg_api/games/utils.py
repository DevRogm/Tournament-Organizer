def get_winner(player_1, player_2, score_1, score_2):
    if score_1 > score_2:
        return player_1
    elif score_1 < score_2:
        return player_2
    else:
        return None

def move_winner():
    pass