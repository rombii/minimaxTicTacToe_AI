def whichsquare(x, y):
    if x <= 150 and y <= 150:
        return 1

    if 160 <= x <= 250 and y <= 150:
        return 2

    if x >= 260 and y <= 150:
        return 3

    if x <= 150 and 160 <= y <= 250:
        return 4

    if 160 <= x <= 250 and 160 <= y <= 250:
        return 5

    if x >= 260 and 160 <= y <= 250:
        return 6

    if x <= 150 and y >= 260:
        return 7

    if 160 <= x <= 250 and 260 <= y <= 370:
        return 8

    if x >= 260 and y >= 260:
        return 9
