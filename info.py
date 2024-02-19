import pygame
from player import Player


class GameInfo:
    lives = 10
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
            #if time_surf != 0 and lives_surf !=0:
            #    imagew = pygame.image.load('images/trophy.jpg').convert_alpha()
            #    image2 = pygame.transform.scale(imagew, (720, 720))
            #    game_win_surf = self.font.render("You won", True, self.game_over_color)
            #    game_win_rect = game_win_surf.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            #    self.screen.blit(image2, (0, 0))
            #    self.screen.blit(game_win_surf, game_win_rect)

        else:
            self.screen.fill((0, 0, 0))
            # Render the game over message
            game_over_surf = self.font.render("Game Over", True, self.game_over_color)
            # Center the game over message on the screen
            game_over_rect = game_over_surf.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(game_over_surf, game_over_rect)

    def won(self):
        imagew = pygame.image.load('images/trophy.jpg').convert_alpha()
        image2 = pygame.transform.scale(imagew, (720, 720))
        smallfont = pygame.font.Font("images/font.ttf", 50)
        game_win_surf = smallfont.render('quit', True, (255, 0, 0))
        #game_win_surf = self.font.render("You won", True, self.game_over_color)
        game_win_rect = game_win_surf.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(image2, (0, 0))
        self.screen.blit(game_win_surf, game_win_rect)

