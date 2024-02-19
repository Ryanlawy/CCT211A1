import pygame
import platforms
"""
Image Used:

level 1 background:
https://www.freepik.com/free-vector/pixel-art-rural-landscape-background_...
level 2 background:
https://www.freepik.com/free-vector/fantastic-space-landscape-martian-alien-...
level 3 background:
https://www.freepik.com/free-vector/pixel-art-vacation-background_29019073.h...


"""
screen_width = 720
class Level():
    """ class that define levels"""

    # a List of sprites used in levels
    platform_list = None
    steponwater_list = None
    steponfire_list = None
    ghost = None
    # background
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -2000

    def __init__(self, player):
        """ initi everything"""
        self.platform_list = pygame.sprite.Group()
        self.steponwater_list = pygame.sprite.Group()
        self.steponfire_list = pygame.sprite.Group()
        self.ghost = pygame.sprite.Group()
        self.player = player


    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.steponwater_list.update()
        self.steponfire_list.update()
        self.ghost.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill((0, 0, 0))
        screen.blit(self.background, (self.world_shift // 3,0))

        # Draw all the sprites
        self.platform_list.draw(screen)
        self.steponwater_list.draw(screen)
        self.steponfire_list.draw(screen)
        self.ghost.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.steponwater_list:
            platform.rect.x += shift_x

        for platform in self.steponfire_list:
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

        background = pygame.image.load("images/levelonebackground.jpg").convert()
        scale_background = pygame.transform.scale(background, (3000, 720))
        self.background = scale_background
        self.background.set_colorkey((25, 25, 25))
        self.level_limit = -1600

        # Array with type of platform, and x(further), y(height < Smaller-higher) location of the platform.

        level = [["Grass", 500, 400], ["Grass", 400, 550],
                 ["Grass", 600, 250], ["Grass", 700, 250],
                 ["Grass", 1000, 250], ["Grass", 1100, 250],
                 ["Grass", 1200, 400], ["Grass", 1300, 500],

                # boundary
                 ["Wall", 0, 650], ["Wall", 0, 580],
                 ["Wall", 0, 510], ["Wall", 0, 440],
                 ["Wall", 0, 370], ["Wall", 0, 300],
                 ["Wall", 0, 230], ["Wall", 0, 160],
                 ["Wall", 3000, 650], ["Wall", 3000, 580],
                 ["Wall", 3000, 510], ["Wall", 3000, 440],
                 ["Wall", 3000, 370], ["Wall", 3000, 300],

                 ["Wall", 1750, 650], ["Wall", 1750, 580],
                 ["Wall", 1750, 510], ["Wall", 1750, 440],
                 ["Wall", 1750, 370], ["Wall", 1750, 300],

                 ["Grass", 2000, 400], ["Grass", 2200, 500],
                 ["House", 2400, 250],
                 #Flag
                 ["Flag", 2720, 200]
                 ]

        step_on_water = [["Water", 800, 250], ["Water", 870, 250],
                   ["Water", 1000, 250], ["Water", 1070, 250],
                  ]



        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for p in step_on_water:
            block = platforms.Platform(p[0])
            block.rect.x = p[1]
            block.rect.y = p[2]
            block.player = self.player
            self.steponwater_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform("Wall")
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add the ground to the map

        ground = platforms.Ground()
        ground.rect.x = 0  # Start at the leftmost part of the level
        ground.rect.y = 650  # Position at the bottom
        ground.player = self.player
        ground.level = self
        # Adjust the width to match the level width
        ground.image = pygame.transform.scale(ground.image, (3000, ground.image.get_height()))
        self.platform_list.add(ground)


class Level_2(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        background = pygame.image.load("images/level2background.jpg").convert()
        scale_background = pygame.transform.scale(background, (3000, 720))
        self.background = scale_background
        self.background.set_colorkey((25, 25, 25))
        self.level_limit = -1600

        # Array with type of platform, and x(further), y(height < Smaller-higher) location of the platform.

        level = [["Grass", 400, 400], ["Grass", 300, 550],
                 ["Wall", 900, 250], ["Wall", 1000, 250],
                 ["Wall", 1800, 300], ["Wall", 1900, 300],
                 ["Wall", 2000, 300], ["Wall", 2100, 300],
                 ["Wall", 1500, 500], ["Wall", 1600, 450],

                 ["Wall", 3000, 650], ["Wall", 3000, 580],
                 ["Wall", 3000, 510], ["Wall", 3000, 440],
                 ["Wall", 3000, 370], ["Wall", 3000, 300],

                 ["House", 500, 250], ["House", 2550, 250],
                    # Flag
                 ["Flag", 2850, 200],



                 # boundary
                 ["Wall", 0, 650], ["Wall", 0, 580],
                 ["Wall", 0, 510], ["Wall", 0, 440],
                 ["Wall", 0, 370], ["Wall", 0, 300],
                 ["Wall", 0, 230], ["Wall", 0, 160],
                 ["Wall", 3000, 650], ["Wall", 3000, 580],
                 ["Wall", 3000, 510], ["Wall", 3000, 440],
                 ["Wall", 3000, 370], ["Wall", 3000, 300],


                 ]

        step_on_fire = [["Fire", 1200, 250], ["Fire", 1270, 250],
                        ["Fire", 2000, 650], ["Fire", 2070, 650],
                        ["Fire", 2140, 650], ["Fire", 2210, 650],
                        ["Fire", 2280, 650]
                        ]



        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in step_on_fire:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.steponfire_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform("Wall")
        block.rect.x = 2300
        block.rect.y = 350
        block.boundary_top = 200
        block.boundary_bottom = 600
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add the ground to the map

        ground = platforms.Ground()
        ground.rect.x = 0  # Start at the leftmost part of the level
        ground.rect.y = 650  # Position at the bottom
        ground.player = self.player
        ground.level = self
        # Adjust the width to match the level width
        ground.image = pygame.transform.scale(ground.image, (3000, ground.image.get_height()))
        self.platform_list.add(ground)



class Level_3(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        background = pygame.image.load("images/level3background.jpg").convert()
        scale_background = pygame.transform.scale(background, (3000, 720))
        self.background = scale_background
        self.background.set_colorkey((25, 25, 25))
        self.level_limit = -1600

        # Array with type of platform, and x(further), y(height < Smaller-higher) location of the platform.

        level = [
                ["Grass", 500, 400], ["Grass", 400, 400],
                 ["Grass", 600, 400], ["Grass", 200, 500],
                ["Grass", 800, 250], ["Grass", 1900, 300],

                ["Grass", 2000, 300], ["Grass", 2100, 300],

                 ["Grass", 2200, 300], ["Grass", 2300, 300],
                 ["Grass", 2400, 300], ["Grass", 2500, 300],
                 ["Grass", 2600, 300], ["Grass", 2700, 300],
                ["Grass", 1500, 400],



                 # boundary
                 ["Wall", 0, 650], ["Wall", 0, 580],
                 ["Wall", 0, 510], ["Wall", 0, 440],
                 ["Wall", 0, 370], ["Wall", 0, 300],
                 ["Wall", 0, 230], ["Wall", 0, 160],

                    # Flag
                ["Flag", 2720, 200], ["House", 2550, 250],
                 ]

        step_on_fire = [["Fire", 1100, 240], ["Fire", 1170, 240],
                        ["Fire", 1400, 240], ["Fire", 1470, 240],]

        step_on_water = [["Water", 800, 650], ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for platform in step_on_fire:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.steponfire_list.add(block)

        for platform in step_on_water:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.steponwater_list.add(block)


        # Add a moving left to right platform 1
        #block = platforms.MovingPlatform("Wall")
        #block.rect.y = 280
        #block.boundary_left = 1350
        #block.boundary_right = 1600
        #block.change_x = 2
        #block.player = self.player
        #block.level = self
        #self.platform_list.add(block)

        # Add a moving left to right platform 2
        #block = platforms.MovingPlatform("Grass")
        #block.rect.x = 2000
        #block.rect.y = 280
        #block.boundary_left = 1350
        #block.boundary_right = 1600
        #block.change_x = 1
        #block.player = self.player
        #block.level = self
        #self.platform_list.add(block)

        # Add a moving left to right platform 3
        block = platforms.MovingPlatform("House")
        block.rect.x = 1500
        block.rect.y = 400
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving up and down platform 1
        #block = platforms.MovingPlatform("Grass")
        #block.rect.x = 2000
        #block.rect.y = 280
        #block.boundary_top = 200
        #block.boundary_bottom = 600
        #block.change_y = 1
        #block.player = self.player
        #block.level = self
        #self.platform_list.add(block)

        # Add a moving up and down platform 2
        block = platforms.MovingPlatform("Wall")
        block.rect.x = 1300
        block.rect.y = 280
        block.boundary_top = 200
        block.boundary_bottom = 600
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving up and down platform 3
        block = platforms.MovingPlatform("Wall")
        block.rect.x = 1600
        block.rect.y = 280
        block.boundary_top = 200
        block.boundary_bottom = 600
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a moving up and down platform 4
        block = platforms.MovingPlatform("Wall")
        block.rect.x = 1000
        block.rect.y = 280
        block.boundary_top = 200
        block.boundary_bottom = 600
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add the ground to the map
        ground = platforms.Ground()
        ground.rect.x = 0  # Start at the leftmost part of the level
        ground.rect.y = 650  # Position at the bottom
        ground.player = self.player
        ground.level = self
        # Adjust the width to match the level width
        ground.image = pygame.transform.scale(ground.image, (3000, ground.image.get_height()))
        self.platform_list.add(ground)
