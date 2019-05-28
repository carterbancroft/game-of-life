# Entrypoint file for Conway's Game of Life implementation. Handles running
# the game and rendering to the screen using pygame.
#
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# 3rd party
import yaml
import math
import random
import pygame

# Project level
import cell_states
import world as world_helper

# Import configuration
with open('config.yml', 'r') as the_yaml:
    cfg = yaml.safe_load(the_yaml)

cell_color = (0, 175, 50) # Cell color in RGB

# Renders a specific world state to the window.
def renderWorld(win, world, color_type):
    # Iterate over our 2D array and draw circles where there is an Alive state.
    for row in range(len(world)):
        for col in range(len(world[row])):
            if world[row][col] == cell_states.dead:
                # This cell is dead, move along.
                continue

            cell_size = cfg['cell_size']

            # Determine the radius of the circle we'll draw based on the calc'd
            # size of the cell.
            radius = int(cell_size / 2)

            # Find the center coordinates of our circle
            center_x = col * cell_size + radius
            center_y = row * cell_size + radius

            # Get the cell color based on the current color type setting
            color = None
            if color_type == 0: color = cell_color
            elif color_type == 1: color = getGradientCellColor(col, len(world[0]))
            elif color_type == 2: color = getRandomCellColor()

            pygame.draw.circle(win, color, (center_x, center_y), radius)


# Get a fancy gradient color based on the column positioning
# TODO: Maybe these color helpers should go elsewhere...
def getGradientCellColor(col, total_cols):
    # Far left should be (255, 0, 0)
    # Middle should be (0, 255, 0)
    # Far right should be (0, 0, 255)

    # Distribution is basically how much a given color should increase or
    # decrease by per column.
    distribution = math.floor(255 / total_cols)

    # Red will decrease from left to right, starting at around 255.
    red = 255 - (col * distribution)

    # Blue will increase from left to right, starting at 0.
    blue = col * distribution

    # Green will increase from left to right until the middle column and then
    # Decrease from left to right after the middle column.
    middle_column = math.floor(total_cols / 2)
    green = None
    if (col <= middle_column):
        green = col * distribution * 2
    else:
        # col - middle_column here makes the middle column act as 0 (the far
        # left in other words).
        green = 255 - ((col - middle_column) * distribution * 2)

    return (red, green, blue)


# Get a random color for the alive cell. This is much more straight forward.
def getRandomCellColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)


# The main function, which handles setting up the window and calling all other
# functions.
def main():
    pygame.init()

    win = pygame.display.set_mode((cfg['screen_width'], cfg['screen_height']))
    pygame.display.set_caption('Life')

    cell_size = cfg['cell_size']
    cell_count_across = int(cfg['screen_width'] / cell_size)
    cell_count_down = int(cfg['screen_height'] / cell_size)

    world = world_helper.generateSeed(cell_count_across, cell_count_down)

    color_type = cfg['starting_color_type']

    run = True
    while run:
        # Events listener. Right now it's only listening for QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        # Clear the screen
        win.fill((0, 0, 0))

        # Update the world object based on the rules for the next tick
        world_helper.updateWorld(world)

        # Render it
        renderWorld(win, world, color_type)

        pygame.display.update()
        pygame.time.delay(cfg['tick_delay'])

    pygame.quit()

# Entrypoint
main()
