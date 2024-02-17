import pygame

from sheet import SpriteSheet


"""
Platform Type:
    1. Moving Platform 
    2. Ground Platform
    3. Air Platform 
    4. Wall 

"""

class Platform(pygame.sprite.Sprite):
    """Platform"""

    def __init__(self, sprite_sheet_data):
        """"""
        pygame.sprite.Sprite.__init__(self)
        # platform
        self.image = 



class LeftToRightPlatform(Platform):
    """ """




# # class UpAndDownPlatform(Platform):
# #     """ """
# import pygame

# WIDTH = 400
# HEIGHT = 300
# BACKGROUND = (0, 0, 0)

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     clock = pygame.time.Clock()

#     while True:
#         screen.fill(BACKGROUND)
#         pygame.display.flip()

#         clock.tick(60)

# if __name__ == "__main__":
#     main()