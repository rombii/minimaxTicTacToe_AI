import random

from checkLose import check_game_end


def select_best_move(possible_moves, game_field):
    bestScore = -1000
    for move in possible_moves:
        possible_moves.remove(move)
        game_field[move - 1] = 'x'
        score = minimax(possible_moves, game_field, False)
        print(move, score)
        game_field[move - 1] = ''
        possible_moves.append(move)
        possible_moves.sort()
        if score > bestScore:
            bestScore = score
            best_move = move
    if bestScore == -100:
        best_move = random.choice(possible_moves)
    return best_move


def minimax(possible_moves, game_field, player):
    if check_game_end('x', game_field):
        if player:
            return 100
        else:
            return -100
    for move in possible_moves:
        possible_moves.remove(move)
        game_field[move - 1] = 'x'
        score = minimax(possible_moves, game_field, not player)
        game_field[move - 1] = ''
        possible_moves.append(move)
        bestScore = score
    return bestScore
