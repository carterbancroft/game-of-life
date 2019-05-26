# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import pygame
import random

import world_helper

# Variables for window size and cell counts etc
# TODO Make it so unequal width/height ratios work
screen_width = 950
screen_height = 950
cell_size = 10
cell_count_across = int(screen_width / cell_size)
cell_count_down = int(screen_height / cell_size)

#print(f'cell_count_across {cell_count_across}')
#print(f'cell_count_down {cell_count_down}')

# All the possible states of a cell
alive = 'a'
dead = '.'
dying = 'd'
being_born = 'b'


# Renders a specific world state to the window.
def renderWorld(win, world):
    #alive_count = 0
    #dead_count = 0

    # Iterate over our 2D array and draw circles where there is an Alive state.
    for row in range(len(world)):
        for cell in range(len(world[row])):
            if world[row][cell] == dead:
                # This cell is dead, move along.
                #dead_count += 1
                #print('dead')
                continue

            # Determine the radius of the circle we'll draw based on the calc'd
            # size of the cell.
            radius = int(cell_size / 2)

            # Find the center coordinates of our circle
            center_x = row * cell_size + radius
            center_y = cell * cell_size + radius

            pygame.draw.circle(win, (0, 0, 255), (center_x, center_y), radius)

            #alive_count += 1

    #print(f'alive: {alive_count}')
    #print(f'dead: {dead_count}')


# The main function, which handles setting up the window and calling all other
# functions.
def main():
    pygame.init()

    win = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Life')

    world = world_helper.generateSeed(cell_count_across, cell_count_down)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Render the current world state
        win.fill((0, 0, 0))
        renderWorld(win, world)
        pygame.display.update()

        # Update the world based on the rules for the next tick
        world_helper.updateWorld(world)

        pygame.time.delay(10)

    pygame.quit()

# Entrypoint.
main()
