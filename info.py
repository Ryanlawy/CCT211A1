import pygame
from player import Player
import Game

class GameInfo:
    lives = 5
    def __init__(self, screen, initial_time):
        self.screen = screen
        self.time = initial_time  # Countdown time in seconds
        self.font = pygame.font.Font("images/font.ttf", 36)  # Use a default font and set the size

        # Colors
        self.text_color = (0, 0, 0)

    def update(self, delta):
        """Update the countdown timer."""
        self.time -= delta  # Subtract the time passed (delta) from the total time

    def draw(self):
        """Draw the time and lives on the screen."""
        # Render the time
        time_surf = self.font.render(f"Time: {int(self.time)}", True, self.text_color)
        self.screen.blit(time_surf, (10, 10))  # Position: top-left corner

        # Render the lives
        lives_surf = self.font.render(f"Lives: {self.lives}", True, self.text_color)
        self.screen.blit(lives_surf, (10, 50))  # Position: slightly below the time

    #def lose_life(self):
    #    """Handle the player losing a life."""
    #    self.lives -= 1
