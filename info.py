import pygame
from player import Player
import Game

class GameInfo:
    lives = 5
    game_over = False
    def __init__(self, screen, initial_time):
        self.screen = screen
        self.time = initial_time  # Countdown time in seconds
        self.font = pygame.font.Font("images/font.ttf", 36)  # Use a default font and set the size

        # Colors
        self.text_color = (0, 0, 0)
        self.game_over_color =(255, 0, 0)
        


    def update(self, delta):
        """Update the countdown timer."""
        if not self.game_over:
            self.time -= delta  # Subtract the time passed (delta) from the total time
            if GameInfo.lives <= 0:
                self.game_over = True

    def draw(self):
        """Draw the time and lives on the screen."""
        # Render the time
        if not self.game_over:
            time_surf = self.font.render(f"Time: {int(self.time)}", True, self.text_color)
            self.screen.blit(time_surf, (10, 10))  # Position: top-left corner

        # Render the lives
            lives_surf = self.font.render(f"Lives: {self.lives}", True, self.text_color)
            self.screen.blit(lives_surf, (10, 50))  # Position: slightly below the time
        else:
            self.screen.fill((0, 0, 0))
            # Render the game over message
            game_over_surf = self.font.render("Game Over", True, self.game_over_color)
            # Center the game over message on the screen
            game_over_rect = game_over_surf.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(game_over_surf, game_over_rect)




