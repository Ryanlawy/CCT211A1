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
smallfont = pygame.font.Font("images/font.ttf", 35)

quit_button_rect = pygame.Rect(430, height / 2, 200, 80)
start_button_rect = pygame.Rect(80, height / 2, 200, 80)


# rendering a text written in
# this font
text1 = smallfont.render('quit', True, color)
text2 = smallfont.render('start', True, color)

# For the 'quit' button
text1_rect = text1.get_rect(center=quit_button_rect.center)
screen.blit(text1, text1_rect)

# For the 'start' button
text2_rect = text2.get_rect(center=start_button_rect.center)
screen.blit(text2, text2_rect)


# Text init#
X = 500
Y = 500
white = (255, 255, 255)
blue = (0, 0, 128)
red = (255,0,0)
black =(0,0,0)

#display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font("images/font.ttf", 100)

text = font.render('Super Steven', True, white)
textRect = text.get_rect()
textRect.center = (360, Y // 4)

"""credit"""
font = pygame.font.Font("images/font.ttf", 10)

credit = font.render('credits by CCT211 week4 sample', True, blue)
creditRect = text.get_rect()
creditRect.center = (900, Y // 4)

"""intro fire"""
image = pygame.image.load('images/fire.jpg').convert_alpha()
image = pygame.transform.scale(image, (50, 50))

font = pygame.font.Font("images/font.ttf", 20)

fire = font.render('Steps on fires will let the player going backwards', True, black)
fireRect = text.get_rect()
fireRect.center = (480, 700)

"""intro water"""
image2 = pygame.image.load('images/water.jpg').convert_alpha()
image2 = pygame.transform.scale(image, (50, 50))

font = pygame.font.Font("images/font.ttf", 20)

water = font.render('Steps on water will make the player stucks', True, black)
waterRect = text.get_rect()
waterRect.center = (480, 650)

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
                Game.main()

    # background
    # screen.fill((0, 0, 0))
    screen.blit(scale_background, (0, 0))

    # stores the (x,y) coordinates into
    mouse = pygame.mouse.get_pos()


    # if mouse is hovered on a button it
    # changes to lighter shade
    # Button colors based on mouse hover
    if quit_button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, color_light, quit_button_rect)
    else:
        pygame.draw.rect(screen, color_dark, quit_button_rect)

    if start_button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, color_light, start_button_rect)
    else:
        pygame.draw.rect(screen, color_dark, start_button_rect)

    # Center and blit the text for each button
    text1_rect = text1.get_rect(center=quit_button_rect.center)
    screen.blit(text1, text1_rect)

    text2_rect = text2.get_rect(center=start_button_rect.center)
    screen.blit(text2, text2_rect)



    # # superimposing the text onto our button
    screen.blit(text, textRect)
    
    screen.blit(credit, creditRect)

    screen.blit(fire, fireRect)

    screen.blit(image, (50, 620))

    screen.blit(water, waterRect)

    screen.blit(image2, (50, 550))

    

    """Intro Text"""

    # updates the frames of the game
    pygame.display.update()


