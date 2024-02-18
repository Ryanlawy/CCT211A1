import pygame

"""
Platform Type:
    1. Moving Platform 
    3. Air Platform 
    4. Wall 
    5. Fire and Water 

"""
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

# Grass
GRASS_PLATFORM = (576, 720, 100, 70)


class Platform(pygame.sprite.Sprite):
    """Platform"""

    def __init__(self):
        """"""
        pygame.sprite.Sprite.__init__(self)
        # platform
        image = pygame.image.load("images/platformgrass.jpg").convert()
        scale_image = pygame.transform.scale(image, (100, 70))
        self.image = scale_image
        #self.image = image
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """A platform that can move left to right"""

    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ platform moving"""

        # change x position
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        # change y position
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:

            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


# Wall class
class Wall(Platform):
    """ Wall"""
    def __init__(self):  # Your parameters here
        super().__init__()
        self.image = pygame.image.load("images/wall.jpg").convert()


# obsticle Classes
class FirePlatform(Platform):
    """ A platform that kills(return to the beginning) the player"""
    def __init__(self):  # Your parameters here
            super().__init__()
            self.image = pygame.image.load("images/fire.jpg").convert()



class WaterPlatform(Platform):
    """ A platform that slows the player"""
    def __init__(self):  # Your parameters here
            super().__init__()
            self.image = pygame.image.load("images/water.jpg").convert()


class Ground(Platform):
    def __init__(self):  # Your parameters here
        super().__init__()
        image1 = pygame.image.load("images/platformgrass.jpg").convert()
        scale_image = pygame.transform.scale(image1, (1000, 70))
        self.image = scale_image
