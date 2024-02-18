import pygame
import platform


class Level():
    """ class that define levels"""

    # a List of sprites used in levels
    platform_list = None
    ghost = None
    # background
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000


    def __init__(self, player):
        """ initi everything"""
        self.platform_list = pygame.sprite.Group()
        self.ghost = pygame.sprite.Group()
        self.player = player


    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.ghost.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill((0, 0, 0))
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprites
        self.platform_list.draw(screen)
        self.ghost.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        ###### might need change #####
        for enemy in self.ghost:
            enemy.rect.x += shift_x


# level 1 map
class Level_1(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("images/levelonebackground.jpg").convert()
        self.background.set_colorkey((25, 25, 25))
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platform.GRASS_PLATFORM, 500, 500],
                  [platform.GRASS_PLATFORM, 570, 500],
                  [platform.GRASS_PLATFORM, 640, 500],
                  [platform.GRASS_PLATFORM, 800, 400],
                  [platform.GRASS_PLATFORM, 870, 400],
                  [platform.GRASS_PLATFORM, 940, 400],
                  [platform.GRASS_PLATFORM, 1000, 500],
                  [platform.GRASS_PLATFORM, 1070, 500],
                  [platform.GRASS_PLATFORM, 1140, 500],
                  [platform.GRASS_PLATFORM, 1120, 280],
                  [platform.GRASS_PLATFORM, 1190, 280],
                  [platform.GRASS_PLATFORM, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platform.Platform(0)
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platform.MovingPlatform(platform.GRASS_PLATFORM)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
