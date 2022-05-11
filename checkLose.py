def checkmove(mov, char, game_field):
    if mov == 1:
        if game_field[1] == char and game_field[2] == char:
            return True
        elif game_field[3] == char and game_field[6] == char:
            return True
        elif game_field[4] == char and game_field[8] == char:
            return True
        return False

    elif mov == 2:
        if game_field[0] == char and game_field[2] == char:
            return True
        elif game_field[4] == char and game_field[7] == char:
            return True
        return False

    elif mov == 3:
        if game_field[5] == char and game_field[8] == char:
            return True
        elif game_field[1] == char and game_field[0] == char:
            return True
        elif game_field[4] == char and game_field[6] == char:
            return True
        return False

    elif mov == 4:
        if game_field[0] == char and game_field[6] == char:
            return True
        elif game_field[4] == char and game_field[5] == char:
            return True
        return False

    elif mov == 5:
        if game_field[3] == char and game_field[5] == char:
            return True
        elif game_field[1] == char and game_field[7] == char:
            return True
        elif game_field[0] == char and game_field[8] == char:
            return True
        elif game_field[2] == char and game_field[6] == char:
            return True
        return False

    elif mov == 6:
        if game_field[2] == char and game_field[8] == char:
            return True
        elif game_field[3] == char and game_field[4] == char:
            return True
        return False

    elif mov == 7:
        if game_field[7] == char and game_field[8] == char:
            return True
        elif game_field[0] == char and game_field[3] == char:
            return True
        elif game_field[2] == char and game_field[4] == char:
            return True
        return False

    elif mov == 8:
        if game_field[6] == char and game_field[8] == char:
            return True
        elif game_field[1] == char and game_field[4] == char:
            return True
        return False

    elif mov == 9:
        if game_field[6] == char and game_field[7] == char:
            return True
        elif game_field[2] == char and game_field[5] == char:
            return True
        elif game_field[0] == char and game_field[4] == char:
            return True
        return False
