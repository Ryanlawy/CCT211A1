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
        image1 = pygame.image.load("images/ghost1.png")
        image1 = pygame.transform.scale(image1, (50, 50))
        image1.set_colorkey((28, 28, 36))
        self.moving_frame.append(image1)
        image = pygame.image.load("images/ghost2.png")
        image_c = pygame.transform.scale(image, (50, 50))
        image_c.set_colorkey((28, 28, 36))
        self.moving_frame.append(image_c)
        image = pygame.image.load("images/ghost1.png")
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
        dirvect = pygame.math.Vector2((player.rect.x - 0) - self.rect.x,
                                      (player.rect.y - 0) - self.rect.y)

        if dirvect.length() != 0:  # Ensure the vector is not zero before normalizing
            dirvect.normalize()
            dirvect.scale_to_length(self.velocity)
            self.rect.move_ip(dirvect)
        else:
            # Handle the case where the ghost has "caught" the player
            GameInfo.lives -= 1
            self.rect.x, self.rect.y = (250, 250)  # Reset position if needed
