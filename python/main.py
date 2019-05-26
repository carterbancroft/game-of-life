# Entrypoint file for Conway's Game of Life implementation. Handles running
# the game and and rendering to the screen using pygame.
#
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# 3rd party
import pygame
import random

# Project level
import cell_states
import world as world_helper

# Variables for window size and cell counts etc
screen_width = 1000
screen_height = 700
cell_size = 10
cell_count_across = int(screen_width / cell_size)
cell_count_down = int(screen_height / cell_size)


# Renders a specific world state to the window.
def renderWorld(win, world):
    # Iterate over our 2D array and draw circles where there is an Alive state.
    for row in range(len(world)):
        for col in range(len(world[row])):
            if world[row][col] == cell_states.dead:
                # This cell is dead, move along.
                continue

            # Determine the radius of the circle we'll draw based on the calc'd
            # size of the cell.
            radius = int(cell_size / 2)

            # Find the center coordinates of our circle
            center_x = col * cell_size + radius
            center_y = row * cell_size + radius

            pygame.draw.circle(win, (0, 0, 255), (center_x, center_y), radius)


# The main function, which handles setting up the window and calling all other
# functions.
def main():
    pygame.init()

    win = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('Life')

    world = world_helper.generateSeed(cell_count_across, cell_count_down)

    run = True
    while run:
        # Events listener. Right now it's only listening for QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Clear the screen
        win.fill((0, 0, 0))

        # Update the world object based on the rules for the next tick
        world_helper.updateWorld(world)

        # Render it
        renderWorld(win, world)

        pygame.display.update()
        pygame.time.delay(10)

    pygame.quit()

# Entrypoint
main()
