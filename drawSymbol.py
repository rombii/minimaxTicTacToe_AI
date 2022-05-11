import pygame


def drawx(squareid, background):
    if squareid == 1:
        pygame.draw.line(background, (255, 255, 0), (80, 70), (110, 120), 11)
        pygame.draw.circle(background, (255, 255, 0), (80, 70), 5)
        pygame.draw.circle(background, (255, 255, 0), (110, 120), 5)

        pygame.draw.line(background, (255, 255, 0), (110, 70), (80, 120), 11)
        pygame.draw.circle(background, (255, 255, 0), (111, 70), 5)
        pygame.draw.circle(background, (255, 255, 0), (81, 120), 5)

    elif squareid == 2:
        pygame.draw.line(background, (255, 255, 0), (190, 70), (220, 120), 11)
        pygame.draw.circle(background, (255, 255, 0), (190, 70), 5)
        pygame.draw.circle(background, (255, 255, 0), (220, 120), 5)

        pygame.draw.line(background, (255, 255, 0), (220, 70), (190, 120), 11)
        pygame.draw.circle(background, (255, 255, 0), (221, 70), 5)
        pygame.draw.circle(background, (255, 255, 0), (191, 120), 5)

    elif squareid == 3:
        pygame.draw.line(background, (255, 255, 0), (300, 70), (330, 120), 11)
        pygame.draw.circle(background, (255, 255, 0), (300, 70), 5)
        pygame.draw.circle(background, (255, 255, 0), (330, 120), 5)

        pygame.draw.line(background, (255, 255, 0), (330, 70), (300, 120), 11)
        pygame.draw.circle(background, (255, 255, 0), (331, 70), 5)
        pygame.draw.circle(background, (255, 255, 0), (301, 120), 5)

    elif squareid == 4:
        pygame.draw.line(background, (255, 255, 0), (80, 185), (110, 235), 11)
        pygame.draw.circle(background, (255, 255, 0), (80, 185), 5)
        pygame.draw.circle(background, (255, 255, 0), (110, 235), 5)

        pygame.draw.line(background, (255, 255, 0), (110, 185), (80, 235), 11)
        pygame.draw.circle(background, (255, 255, 0), (111, 185), 5)
        pygame.draw.circle(background, (255, 255, 0), (81, 235), 5)

    elif squareid == 5:
        pygame.draw.line(background, (255, 255, 0), (195, 185), (225, 235), 11)
        pygame.draw.circle(background, (255, 255, 0), (195, 185), 5)
        pygame.draw.circle(background, (255, 255, 0), (225, 235), 5)

        pygame.draw.line(background, (255, 255, 0), (225, 185), (195, 235), 11)
        pygame.draw.circle(background, (255, 255, 0), (226, 185), 5)
        pygame.draw.circle(background, (255, 255, 0), (196, 235), 5)

    elif squareid == 6:
        pygame.draw.line(background, (255, 255, 0), (300, 185), (330, 235), 11)
        pygame.draw.circle(background, (255, 255, 0), (300, 185), 5)
        pygame.draw.circle(background, (255, 255, 0), (330, 235), 5)

        pygame.draw.line(background, (255, 255, 0), (330, 185), (300, 235), 11)
        pygame.draw.circle(background, (255, 255, 0), (331, 185), 5)
        pygame.draw.circle(background, (255, 255, 0), (301, 235), 5)

    if squareid == 7:
        pygame.draw.line(background, (255, 255, 0), (80, 300), (110, 350), 11)
        pygame.draw.circle(background, (255, 255, 0), (80, 300), 5)
        pygame.draw.circle(background, (255, 255, 0), (110, 350), 5)

        pygame.draw.line(background, (255, 255, 0), (110, 300), (80, 350), 11)
        pygame.draw.circle(background, (255, 255, 0), (111, 300), 5)
        pygame.draw.circle(background, (255, 255, 0), (81, 350), 5)

    elif squareid == 8:
        pygame.draw.line(background, (255, 255, 0), (190, 300), (220, 350), 11)
        pygame.draw.circle(background, (255, 255, 0), (190, 300), 5)
        pygame.draw.circle(background, (255, 255, 0), (220, 350), 5)

        pygame.draw.line(background, (255, 255, 0), (220, 300), (190, 350), 11)
        pygame.draw.circle(background, (255, 255, 0), (221, 300), 5)
        pygame.draw.circle(background, (255, 255, 0), (191, 350), 5)

    elif squareid == 9:
        pygame.draw.line(background, (255, 255, 0), (300, 300), (330, 350), 11)
        pygame.draw.circle(background, (255, 255, 0), (300, 300), 5)
        pygame.draw.circle(background, (255, 255, 0), (330, 350), 5)

        pygame.draw.line(background, (255, 255, 0), (330, 300), (300, 350), 11)
        pygame.draw.circle(background, (255, 255, 0), (331, 300), 5)
        pygame.draw.circle(background, (255, 255, 0), (301, 350), 5)


def drawo(squareid, background):
    if squareid == 1:
        pygame.draw.circle(background, (255, 255, 0), (100, 100), 40, 10)
    elif squareid == 2:
        pygame.draw.circle(background, (255, 255, 0), (210, 100), 40, 10)
    elif squareid == 3:
        pygame.draw.circle(background, (255, 255, 0), (320, 100), 40, 10)

    elif squareid == 4:
        pygame.draw.circle(background, (255, 255, 0), (100, 210), 40, 10)
    elif squareid == 5:
        pygame.draw.circle(background, (255, 255, 0), (210, 210), 40, 10)
    elif squareid == 6:
        pygame.draw.circle(background, (255, 255, 0), (320, 210), 40, 10)

    elif squareid == 7:
        pygame.draw.circle(background, (255, 255, 0), (100, 320), 40, 10)
    elif squareid == 8:
        pygame.draw.circle(background, (255, 255, 0), (210, 320), 40, 10)
    elif squareid == 9:
        pygame.draw.circle(background, (255, 255, 0), (320, 320), 40, 10)
