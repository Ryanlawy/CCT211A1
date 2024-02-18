import math
import pygame
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    moving_frame = []
    def __init__(self):
        super().__init__()

        # Animation of ghost
        image1 = pygame.image.load("images/ghost1.jpg").convert()
        image1 = pygame.transform.scale(image1, (50, 50))
        self.moving_frame.append(image1)
        image = pygame.image.load("images/ghost2.jpg").convert()
        image_c = pygame.transform.scale(image, (50, 50))
        self.moving_frame.append(image_c)
        image = pygame.image.load("images/ghost3.jpg").convert()
        image_c = pygame.transform.scale(image, (50, 50))
        self.moving_frame.append(image_c)
        self.image = image1
        self.rect = self.image.get_rect()
        self.speed = 3

    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    # Same thing using only pygame utilities
    def move_towards_player2(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                      player.rect.y - self.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
