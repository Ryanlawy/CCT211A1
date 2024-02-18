# INITIALIZE
import random
import pygame
import Game
from player import Player


# Ghost Class
class Ghost(pygame.sprite.Sprite):
    moving_frame = []

    (SEEK, FLEE, SEPARATE) = range(3)

    def __init__(self, startpos, velocity, startdir):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        # Animation of ghost
        image1 = pygame.image.load("images/ghost1.png").convert()
        image1 = pygame.transform.scale(image1, (50, 50))
        self.moving_frame.append(image1)
        image = pygame.image.load("images/ghost2.png").convert()
        image_c = pygame.transform.scale(image, (50, 50))
        self.moving_frame.append(image_c)
        image = pygame.image.load("images/ghost3.png").convert()
        image_c = pygame.transform.scale(image, (50, 50))
        self.moving_frame.append(image_c)
        self.image = image1
        ###
        self.rect = self.image.get_rect(
            center=(round(self.pos.x), round(self.pos.y)))
        self.state = Ghost.SEEK

    def update(self):

        pos = self.rect.x
        frame = (pos // 30) % len(self.moving_frame)
        self.image = self.moving_frame[frame]

    # Same thing using only pygame utilities
    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                      player.rect.y - self.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.velocity)
        self.rect.move_ip(dirvect)

