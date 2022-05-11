import random

from checkLose import checkmove


def selectbestmove(possible_moves, game_field):
    not_lose_moves = []
    lose_moves = []
    for move in possible_moves:
        if checkmove(move, 'x', game_field): # if lose value == -1
            lose_moves.append(move)
        else:
            not_lose_moves.append(move)
    if len(not_lose_moves) == 0:
        return random.choice(lose_moves)
    return random.choice(not_lose_moves)
