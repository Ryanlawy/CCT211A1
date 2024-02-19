# from pygame.sprite import _Group
# import GlobalStuff
# from spritesheet_functions import SpriteSheet
from platforms import MovingPlatform
import pygame
import info
import level


screen_width = 720
screen_height = 650


class Player(pygame.sprite.Sprite):
    # level bumper
    level = None

    def __init__(self, x, y, lives):
        super().__init__()  # Initialize the sprite superclass
        self.lives = lives
        self.sprite_sheet_image = pygame.image.load('images/walktry.png').convert_alpha()  # load image
        self.change_x = 0  # Movement along X
        self.change_y = 0  # Movement along Y
        self.walking_frames_left = []
        self.walking_frames_right = []
        self.current_frame = 0
        sprite_width = 880  # Width of a single sprite frame in the sheet
        sprite_height = 1550  # Height of a single sprite frame in the sheet
        num_frames = 6  # Total number of frames in the sprite sheet



        for i in range(num_frames):
            # Extract and scale each frame individually
            frame = self.extract_sprite(i * 824, 0, sprite_width, sprite_height)
            scaled_frame = pygame.transform.scale(frame, (100, 150))  # Scale the frame to desired size
            scaled_frame.set_colorkey((255, 0, 0))  # Set white to transparent for the original frame
            self.walking_frames_right.append(scaled_frame)

            # Flip the scaled frame for walking left, then apply the color key to the flipped frame
            flipped_frame = pygame.transform.flip(scaled_frame, True, False)  # Flip the frame
            flipped_frame.set_colorkey((255, 0, 0))  # Set white to transparent for the flipped frame
            self.walking_frames_left.append(flipped_frame)



        self.image = self.walking_frames_right[self.current_frame]
        self.rect = self.image.get_rect()

    def extract_sprite(self, x, y, width, height):
        """Extracts a single sprite from the sprite sheet."""
        frame = pygame.Surface((width, height), pygame.SRCALPHA)
        frame.blit(self.sprite_sheet_image, (-110, 0), (x, y, width, height))
        return frame

    def go_left(self):
        """Moves the player to the left."""
        self.change_x = -8

    def go_right(self):
        """Moves the player to the right."""
        self.change_x = 8

    def stop(self):
        """Stops the player's movement."""
        self.change_x = 0

    def jump(self):
        # Only jump if on the ground
        self.rect.y += 2  # Move down a bit to check if the player is on the ground
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2  # Move back up

        # If it's ok to jump (i.e., on the ground), then jump
        if len(platform_hit_list) > 0 or self.rect.bottom >= 650:
            self.change_y = -15  # Upward movement; adjust as necessary for jump strength
        # self.change_y =-10


    def update(self):

        """check for collision with platforms"""
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
        # If moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if moving left, do the opposite.
                self.rect.left = block.rect.right

            # Gravity
        self.change_y += 0.5  # Adjust the gravity strength as needed
        if self.rect.bottom > screen_height:
            self.change_y = 0
            self.rect.bottom = screen_height
        elif self.rect.top < 0:
            self.change_y = 0
            self.rect.top = 0

        # Check for collision with platforms during vertical movement
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            # Stop vertical movement
            self.change_y = 0

        """Updates the player's position and simulates gravity."""
        self.rect.x += self.change_x
        self.current_frame = (self.current_frame + 1) % len(self.walking_frames_right)
        if self.change_x > 0:
            self.image = self.walking_frames_right[self.current_frame]
        elif self.change_x < 0:
            self.image = self.walking_frames_left[self.current_frame]

        ### check left right
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        # Check top bottom
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            # self.change_y = 0
            # self.change_x = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x


        # step on Fire
        block_hit_list1 = pygame.sprite.spritecollide(self, self.level.steponfire_list, False)
        for block in block_hit_list1:
            # If we are moving right,
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.top = block.rect.bottom

            self.change_x -= 3

        # step on water
        block_hit_list1 = pygame.sprite.spritecollide(self, self.level.steponwater_list, False)
        for block in block_hit_list1:
            # If we are moving right,
            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.top = block.rect.bottom

            self.change_x +=3
