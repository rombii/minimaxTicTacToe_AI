import random

from checkLose import check_game_end
countW, countL = 0, 0


def select_best_move(possible_moves, game_field):
    bestScore = -1000
    global countW, countL
    bestCount = 0
    bestMove = None
    for move in possible_moves:
        countW = 0
        countL = 0
        possible_moves.remove(move)
        game_field[move - 1] = 'x'
        score = minimax(possible_moves, game_field, False)
        print(move, score, countW/(countL+countW))
        game_field[move - 1] = ''
        possible_moves.append(move)
        possible_moves.sort()
        if score >= bestScore and countW/(countL+countW) > bestCount:
            bestScore = score
            bestMove = move
            bestCount = countW/(countL+countW)

    if bestMove is None:
        bestMove = random.choice(possible_moves)
    return bestMove


def minimax(possible_moves, game_field, player):
    global countW, countL
    if check_game_end('x', game_field):
        if player:
            countW += 1
            return 100
        else:
            countL += 1
            return -100
    if player:
        bestScore = 100
    else:
        bestScore = -100
    for move in possible_moves:
        possible_moves.remove(move)
        game_field[move - 1] = 'x'
        score = minimax(possible_moves, game_field, not player)
        game_field[move - 1] = ''
        possible_moves.append(move)
        possible_moves.sort()
        if player:
            bestScore = min(bestScore, score)
        else:
            bestScore = max(bestScore, score)
    return bestScore
