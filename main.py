import pygame.font
from pygame.locals import *

from checkLose import check_move
from drawBackground import draw_background
from drawSymbol import *
from minimax import select_best_move
from squareSelect import which_square


def main():
    possible_move = list(range(1, 10))
    game_field = ['', '', '', '', '', '', '', '', '']
    game_ended = False
    player_lost = True  # true = player, false = bot
    pygame.init()
    size = width, height = 420, 420
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic, Tac, Toe")

    background = draw_background(screen)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    end_screen = pygame.Surface(screen.get_size())
    end_screen = end_screen.convert()
    end_screen.fill((255, 255, 0))
    end_screen.set_alpha(100)
    font = pygame.font.Font(pygame.font.match_font('verdana'), 72)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if game_ended:
                try:
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            pygame.display.quit()
                            main()
                            draw_background(screen)
                            break
                except pygame.error:
                    print("See you soon!")


            if not game_ended:
                if event.type == MOUSEBUTTONDOWN:
                    if 50 <= event.pos[0] <= 370 and 50 <= event.pos[1] <= 370:
                        selectedSquare = which_square(event.pos[0], event.pos[1])
                        if selectedSquare in possible_move:
                            draw_x(selectedSquare, background)
                            game_field[selectedSquare - 1] = 'x'
                            possible_move.remove(selectedSquare)
                            game_ended = check_move(selectedSquare, 'x', game_field)
                            player_lost = True
                            if len(possible_move) != 0 and not game_ended:
                                bot_choice = select_best_move(possible_move, game_field)
                                draw_x(bot_choice, background)
                                game_field[bot_choice - 1] = 'x'
                                possible_move.remove(bot_choice)
                                game_ended = check_move(bot_choice, 'x', game_field)
                                player_lost = False

        screen.blit(background, (0, 0))
        if game_ended:
            screen.blit(end_screen, (0, 0))
            if player_lost:
                text = font.render('You lost', True, (22, 22, 22))
            else:
                text = font.render('You Won', True, (22, 22, 22))
            text_rect = text.get_rect()
            text_rect.center = (width // 2, height // 2)
            screen.blit(text, text_rect)
            fontr = pygame.font.Font(pygame.font.match_font('verdana'), 24)
            textr = fontr.render('To play again press "R"', True, (22, 22, 22))
            text_rectr = textr.get_rect()
            text_rectr.center = (width // 2, (height // 2) + 100)
            screen.blit(textr, text_rectr)

            # pygame.event.Event(USEREVENT, )
        pygame.display.flip()


if __name__ == '__main__':
    main()
