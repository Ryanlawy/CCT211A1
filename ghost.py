import random
import pygame
import Game
from info import GameInfo



# Ghost Class
class Ghost(pygame.sprite.Sprite):
    moving_frame = []

    (SEEK, FLEE, SEPARATE) = range(3)

    def __init__(self, startpos, velocity):
        super().__init__()
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity

        # Animation of ghost
        image1 = pygame.image.load("images/gh1.png").convert_alpha()
        image1 = pygame.transform.scale(image1, (50, 50))
        image1.set_colorkey((28, 28, 36))
        self.moving_frame.append(image1)
        image = pygame.image.load("images/gh2.png").convert_alpha()
        image_c = pygame.transform.scale(image, (50, 50))
        image_c.set_colorkey((28, 28, 36))
        self.moving_frame.append(image_c)
        image = pygame.image.load("images/gh3.png").convert_alpha()
        image_c = pygame.transform.scale(image, (50, 50))
        image_c.set_colorkey((28, 28, 36))
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
        dirvect = pygame.math.Vector2((player.rect.x - 25) - self.rect.x,
                                      (player.rect.y - 25) - self.rect.y)
        
        try:
            dirvect.normalize()
            # Move along this normalized vector towards the player at current speed.
            dirvect.scale_to_length(self.velocity)
            self.rect.move_ip(dirvect)
        except:
            GameInfo.lives -= 1
            self.rect.x, self.rect.y = (250, 250)
