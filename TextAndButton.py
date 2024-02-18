import pygame
import Game
import os
from subprocess import call

# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)


# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# background picture
background = pygame.image.load("images/start_background2.jpg").convert()
scale_background = pygame.transform.scale(background, (720, 720))

# defining a font
smallfont = pygame.font.SysFont('ariel', 35)

# rendering a text written in
# this font
text1 = smallfont.render('quit', True, color)
text2 = smallfont.render('start', True, color)

# Text init#
X = 500
Y = 500
white = (255, 255, 255)
blue = (0, 0, 128)

#display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont('arial', 100)

#['dejavuserif', 'dejavusansmono', 'dejavusans', 'arial']

text = font.render('Super Steven', True, white)
textRect = text.get_rect()
textRect.center = (360, Y // 4)


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

            if width / 4 <= mouse[0] <= width / 4 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                #start the game
                #call(["python", "Game.py"])
                Game.main()

    # background
    # screen.fill((0, 0, 0))
    screen.blit(scale_background, (0, 0))

    # stores the (x,y) coordinates into
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [
            width / 2, height / 2, 140, 40])

    elif width / 4 <= mouse[0] <= width / 4 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [
            width / 4, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [
            width / 2, height / 2, 140, 40])

        pygame.draw.rect(screen, color_dark, [
            width / 4, height / 2, 140, 40])


    # superimposing the text onto our button
    screen.blit(text1, (width / 2 + 50, height / 2))
    screen.blit(text2, (width / 4 + 50, height / 2))
    screen.blit(text, textRect)

    """Intro Text"""

    # updates the frames of the game
    pygame.display.update()


