import pygame
# from pygame.sprite import _Group
# import GlobalStuff
# from platforms import MovingPlatform
# from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()  # Initialize the sprite superclass
        x = 60
        y = 400
        original_image = pygame.image.load('images/walk1.png').convert_alpha()  # load image
        self.image = pygame.transform.scale(original_image, (100, 150))
        self.rect = self.image.get_rect()  # Get the rectangular area of the Surface
        self.rect.x = x  # Initial X position
        self.rect.y = y  # Initial Y position
        self.change_x = 0  # Movement along X
        self.change_y = 0  # Movement along Y

    def update(self):
        """Update the player's position."""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def go_left(self):
        """Moves the player to the left."""
        self.change_x = -5

    def go_right(self):
        """Moves the player to the right."""
        self.change_x = 5

    def stop(self):
        """Stops the player's movement."""
        self.change_x = 0
    
    def jump(self):
        """Makes the player jump if they are on the ground."""
        self.rect.y += 1  # Move down a bit to check if the player is on the ground
        hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 1  # Move back up

        # If it's ok to jump, set our speed upwards
        if len(hit_list) > 0 or self.rect.bottom >= screen_height:
            self.change_y = -10  # Adjust the jump strength as needed


def update(self):
    """Updates the player's position and simulates gravity."""
    self.rect.x += self.change_x
    self.rect.y += self.change_y

    # Gravity
    self.change_y += 0.35  # Adjust the gravity strength as needed
    if self.rect.bottom > screen_height:
        self.change_y = 0
        self.rect.bottom = screen_height

    

# Example usage
def main():
    pygame.init()

    screen_width = 720
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Super Steve")

    # Create a player instance at position (100, 100)
    player = Player(100, 100)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.stop()

        all_sprites.update()

        screen.fill((255, 255, 255))  # Fill the screen with white
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


# class Player(pygame.sprite.Sprite):
#     """ This class represents the bar at the bottom that the player
#     controls. """

#     # -- Attributes
#     # Set speed vector of player
#     change_x = 0
#     change_y = 0

#     # This holds all the images for the animated walk left/right
#     # of our player
#     walking_frames_l = []
#     walking_frames_r = []

#     # What direction is the player facing?
#     direction = "R"

#     # List of sprites we can bump against
#     level = None
#     def get_image(self, x, y, width, height):
    
#         # Create a new blank image
#         image = pygame.Surface([width, height], pygame.SRCALPHA).convert_alpha()
#         # Copy the sprite from the large sheet onto the smaller image
#         image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
#         # Assuming the sprite's top-left corner is transparent, set color key.
#         image.set_colorkey(image.get_at((0,0)))

#         return image


#     # -- Methods 
#     def __init__(self):
#         """ Constructor function """

#         # Call the parent's constructor
#         pygame.sprite.Sprite.__init__(self)

#         sprite_sheet = pygame.image.load("images/walk.jpg").convert()
#         # Load all the right facing images into a list
#         image = sprite_sheet.get_image(0, 0, 66, 90)
#         self.walking_frames_r.append(image)
#         image = sprite_sheet.get_image(66, 0, 66, 90)
#         self.walking_frames_r.append(image)
#         image = sprite_sheet.get_image(132, 0, 67, 90)
#         self.walking_frames_r.append(image)
#         image = sprite_sheet.get_image(0, 93, 66, 90)
#         self.walking_frames_r.append(image)
#         image = sprite_sheet.get_image(66, 93, 66, 90)
#         self.walking_frames_r.append(image)
#         image = sprite_sheet.get_image(132, 93, 72, 90)
#         self.walking_frames_r.append(image)
#         image = sprite_sheet.get_image(0, 186, 70, 90)
#         self.walking_frames_r.append(image)

#         # Load all the right facing images, then flip them
#         # to face left.
#         image = sprite_sheet.get_image(0, 0, 66, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)
#         image = sprite_sheet.get_image(66, 0, 66, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)
#         image = sprite_sheet.get_image(132, 0, 67, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)
#         image = sprite_sheet.get_image(0, 93, 66, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)
#         image = sprite_sheet.get_image(66, 93, 66, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)
#         image = sprite_sheet.get_image(132, 93, 72, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)
#         image = sprite_sheet.get_image(0, 186, 70, 90)
#         image = pygame.transform.flip(image, True, False)
#         self.walking_frames_l.append(image)

#         # Set the image the player starts with
#         self.image = self.walking_frames_r[0]

#         # Set a referance to the image rect.
#         self.rect = self.image.get_rect()

#     def update(self):
#         """ Move the player. """
#         # Gravity
#         self.calc_grav()

#         # Move left/right
#         self.rect.x += self.change_x
#         pos = self.rect.x + self.level.world_shift
#         if self.direction == "R":
#             frame = (pos // 30) % len(self.walking_frames_r)
#             self.image = self.walking_frames_r[frame]
#         else:
#             frame = (pos // 30) % len(self.walking_frames_l)
#             self.image = self.walking_frames_l[frame]

#         # See if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
#             # If we are moving right,
#             # set our right side to the left side of the item we hit
#             if self.change_x > 0:
#                 self.rect.right = block.rect.left
#             elif self.change_x < 0:
#                 # Otherwise if we are moving left, do the opposite.
#                 self.rect.left = block.rect.right

#         # Move up/down
#         self.rect.y += self.change_y

#         # Check and see if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:

#             # Reset our position based on the top/bottom of the object.
#             if self.change_y > 0:
#                 self.rect.bottom = block.rect.top
#             elif self.change_y < 0:
#                 self.rect.top = block.rect.bottom

#             # Stop our vertical movement
#             self.change_y = 0

#             # if isinstance(block, MovingPlatform):
#             #     self.rect.x += block.change_x

#     def calc_grav(self):
#         """ Calculate effect of gravity. """
#         if self.change_y == 0:
#             self.change_y = 1
#         else:
#             self.change_y += .35

#         # See if we are on the ground.
#         if self.rect.y >= GlobalStuff.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
#             self.change_y = 0
#             self.rect.y = GlobalStuff.SCREEN_HEIGHT - self.rect.height

#     def jump(self):
#         """ Called when user hits 'jump' button. """

#         # move down a bit and see if there is a platform below us.
#         # Move down 2 pixels because it doesn't work well if we only move down 1
#         # when working with a platform moving down.
#         self.rect.y += 2
#         platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         self.rect.y -= 2

#         # If it is ok to jump, set our speed upwards
#         if len(platform_hit_list) > 0 or self.rect.bottom >= GlobalStuff.SCREEN_HEIGHT:
#             self.change_y = -10

#     # Player-controlled movement:
#     def go_left(self):
#         """ Called when the user hits the left arrow. """
#         self.change_x = -6
#         self.direction = "L"

#     def go_right(self):
#         """ Called when the user hits the right arrow. """
#         self.change_x = 6
#         self.direction = "R"

#     def stop(self):
#         """ Called when the user lets off the keyboard. """
#         self.change_x = 0