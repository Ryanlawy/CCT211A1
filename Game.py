
"""
Main Game Loop
"""

"""
TODO:
    1. Ghost
    2. Fire, Water
"""

import pygame
import TextAndButton
import level
from info import GameInfo
from ghost import Ghost
import platforms
from player import Player

def main():
    """Game loop"""
    pygame.init()

    # Set the height and width of the screen
    size = [720, 720]
    screen = pygame.display.set_mode(size)
    game_info = GameInfo(screen, 120)
    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player(100, 100, 5)

    # Create all the levels
    level_list = []
    level_list.append(level.Level_1(player))
    level_list.append(level.Level_2(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]


    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 150
    player.rect.y = 720 - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Ghost start
    ghost = Ghost((250, 250), 2)
    active_sprite_list.add(ghost)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    # -------- Main Program Loop -----------
    while not done:
        delta = clock.tick(60) / 1000.0
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # Update game info
        game_info.update(delta)

        # chase

        ghost.move_towards_player(player)
        ghost.update()

        if pygame.sprite.collide_rect(ghost, player):
            GameInfo.lives -=1
            ghost.rect.x, ghost.rect.y=(250,250)

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                pygame.quit()

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        game_info.draw()  # Draw the game info

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()


