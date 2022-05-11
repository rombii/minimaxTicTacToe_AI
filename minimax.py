import random

from checkLose import check_move


def select_best_move(possible_moves, game_field):
    # in this situation where both players are playing with the same sign and connecting three causes defeat the
    # options have 2 values 1 and -1
    # we can check if after this move there is possibility of not losing if it exists try next move
    only_losing_move = False # Is next player move possible without losing
    not_lose_moves = []  # with value 1 and 0
    lose_moves = []  # with value -1
    for move in possible_moves:
        if check_move(move, 'x', game_field):  # if lose value == -1
            lose_moves.append(move)
        else:
            not_lose_moves.append(move)
    if len(not_lose_moves) == 0:
        return random.choice(lose_moves)
    for move in not_lose_moves:
        game_field[move-1] = 'x'
        possible_moves.remove(move)
        only_losing_move = is_next_move_possible(possible_moves, game_field)
        game_field[move-1] = ''
        possible_moves.append(move)
        if only_losing_move:
            return move
    return random.choice(not_lose_moves)


def is_next_move_possible(possible_moves, game_field):
    not_lose_moves = []  # with value 1
    lose_moves = []  # with value -1
    for move in possible_moves:
        if check_move(move, 'x', game_field):  # if lose value == -1
            lose_moves.append(move)
        else:
            not_lose_moves.append(move)
    if len(not_lose_moves) == 0:
        return True
    return False