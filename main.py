import random

import pygame
from pygame.locals import *

from minimax import selectbestmove
from squareSelect import whichsquare
from drawSymbol import *
from checkLose import checkmove

possible_move = list(range(1, 10))
game_field = ['', '', '', '', '', '', '', '', '']
game_ended = False

def main():
    global game_ended
    pygame.init()
    size = width, height = 420, 420
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic, Tac, Toe")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((34, 34, 34))

    pygame.draw.line(background, (255, 255, 255), (50, 155), (370, 155), 10)
    pygame.draw.line(background, (255, 255, 255), (50, 265), (370, 265), 10)

    pygame.draw.line(background, (255, 255, 255), (155, 50), (155, 370), 10)
    pygame.draw.line(background, (255, 255, 255), (265, 50), (265, 370), 10)

    pygame.draw.circle(background, (255, 255, 255), (156, 50), 5)
    pygame.draw.circle(background, (255, 255, 255), (266, 50), 5)

    pygame.draw.circle(background, (255, 255, 255), (156, 370), 5)
    pygame.draw.circle(background, (255, 255, 255), (266, 370), 5)

    pygame.draw.circle(background, (255, 255, 255), (50, 156), 5)
    pygame.draw.circle(background, (255, 255, 255), (370, 156), 5)

    pygame.draw.circle(background, (255, 255, 255), (50, 266), 5)
    pygame.draw.circle(background, (255, 255, 255), (370, 266), 5)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if not game_ended:
                if event.type == MOUSEBUTTONDOWN:
                    if 50 <= event.pos[0] <= 370 and 50 <= event.pos[1] <= 370:
                        selectedSquare = whichsquare(event.pos[0], event.pos[1])
                        if selectedSquare in possible_move:
                            drawx(selectedSquare, background)
                            game_field[selectedSquare-1] = 'x'
                            possible_move.remove(selectedSquare)
                            game_ended = checkmove(selectedSquare, 'x', game_field)
                            if possible_move.__sizeof__() != 0 and not game_ended:
                                botchoice = selectbestmove(possible_move, game_field)
                                drawx(botchoice, background)
                                game_field[botchoice-1] = 'x'
                                possible_move.remove(botchoice)
                                game_ended = checkmove(botchoice, 'x', game_field)

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
