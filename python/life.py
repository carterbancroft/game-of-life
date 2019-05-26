# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import random
from graphics import *

# Variables for window size and cell counts etc
screen_width = 800
screen_height = 800
cell_size = 10
cell_count_across = int(screen_width / cell_size)
cell_count_down = int(screen_height / cell_size)

print(f'cell_count_across {cell_count_across}')
print(f'cell_count_down {cell_count_down}')

# All the possible states of a cell
alive = 'a'
dead = ' '
dying = 'd'
being_born = 'b'

# Randomly generate a starting game state.
def generateWorld():
    # The world will be stored in a 2D array where each space in the array
    # represents a specific cell at a specific point in space. To start, the
    # cell can either be alive or dead. This will kick off the game
    world = []

    for i in range(cell_count_down):
        world_row = []
        for j in range(cell_count_across):
            # Use a random number generator to help us determine whether a cell
            # should be alive or not. Make it relatively rare for life to occur.
            val = random.randint(1, 10001)
            if val >= 9900:
                world_row.append(alive)
            else:
                world_row.append(dead)

        # We've got a row, append it to the world.
        world.append(world_row)

    # Simply return our world representation. Rendering will be handled later.
    return world

# Renders a specific world state to the window.
def renderWorld(win, world):
    # Just some vars to give me insight.
    alive_count = 0
    dead_count = 0

    # Iterate over our 2D array and draw circles where there is an Alive state.
    for row in range(len(world)):
        for cell in range(len(world[row])):
            if world[row][cell] == dead:
                # This cell is dead, move along.
                dead_count += 1
                print('dead')
                continue

            # Nice this cell is alive, render.
            print('alive')

            # Determine the radius of the circle we'll draw based on the calc'd
            # size of the cell.
            radius = int(cell_size / 2)

            # Find the center coordinates of our circle
            center_x = row * cell_size + radius
            center_y = cell * cell_size + radius

            # Define the point where the center of the circle will be rendered.
            point = Point(center_x, center_y)

            # Render our circle (the creature) in the cell. Color it green.
            creature = Circle(point, radius)
            creature.setFill('green')
            creature.draw(win)

            alive_count += 1

    print(alive_count)
    print(dead_count)

# The main function, which handles setting up the window and calling all other
# functions.
def main():
    win = GraphWin('Life', screen_width, screen_height)
    win.setBackground('black')

    world = generateWorld()
    renderWorld(win, world)

    # Shutdown upon mouse click.
    win.getMouse()
    win.close()

# Entrypoint.
main()
