# Handles logic for manipulating and generating the world array. Including the
# rules of Life.

# 3rd party
import random

# Project level
import cell_states

# Randomly generate a starting game state.
def generateSeed(width, height):
    # The world will be stored in a 2D array where each space in the array
    # represents a specific cell at a specific point in space. To start, the
    # cell can either be alive or dead. This will kick off the game
    world = []

    for i in range(height):
        world_row = []
        for j in range(width):
            # Use a random number generator to help us determine whether a cell
            # should be alive or not. Make it relatively rare for life to occur.
            val = random.uniform(0, 1)
            if val >= .90:
                world_row.append(cell_states.alive)
            else:
                world_row.append(cell_states.dead)

        # We've got a row, append it to the world.
        world.append(world_row)

    # Simply return our world representation. Rendering will be handled later.
    return world


# Get a list of all the neighbors of a given cell. This will be used to
# determine the state of the cell in the next generation.
def getNeighbors(world, cell_row, cell_col):
    # Start at the top corner of the 9 cell space that this cell is
    # centered within.
    row = cell_row - 1
    col = cell_col - 1

    neighbors = []

    for i in range(3):
        if row >= len(world): break

        if row < 0:
            row += 1
            continue

        for j in range(3):
            if col >= len(world[j]): break

            if col < 0:
                col += 1
                continue

            if row == cell_row and col == cell_col:
                col += 1
                continue

            neighbors.append(world[row][col])
            col += 1

        col = cell_col - 1
        row += 1

    return neighbors


# Determines the state of a specific cell based on it's current state and the
# state of it's neighbors. This is where the rules live.
#
# Rules:
#   if the current cell is alive then...
#       if it has fewer than 2 lives neighbours it dies
#       if it has 2 OR 3 live neighbours it remains alive, nothing changes
#       if it has > 3 live neighbors it dies
#   if the current cell is dead then...
#       if there are exactly 3 live neighbours then it becomes alive otherwise it stays dead
def determineCellState(neighbors, current_state):

    alive_neighbors = 0
    previously_alive_states = [cell_states.dying, cell_states.alive]
    for neighbor_state in neighbors:
        if neighbor_state in previously_alive_states: alive_neighbors += 1

    new_state = current_state
    if current_state in previously_alive_states:
        if alive_neighbors < 2:
            new_state = cell_states.dying
        if alive_neighbors > 3:
            new_state = cell_states.dying
    else:
        if alive_neighbors == 3: new_state = cell_states.being_born
    
    return new_state


# Updates the world array based on the rules of the game
def updateWorld(world):
    for row in range(len(world)):
        for col in range(len(world[row])):
            neighbors = getNeighbors(world, row, col)
            new_state = determineCellState(neighbors, world[row][col])
            world[row][col] = new_state

    for row in range(len(world)):
        for col in range(len(world[row])):
            if world[row][col] == cell_states.dying:
                world[row][col] = cell_states.dead
            elif world[row][col] == cell_states.being_born:
                world[row][col] = cell_states.alive

