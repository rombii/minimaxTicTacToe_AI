import pygame


def draw_background(screen):
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
    return background


def draw_menu(screen):
    main_menu = pygame.Surface(screen.get_size())
    main_menu = main_menu.convert()
    main_menu.fill((34, 34, 34))

    return main_menu
