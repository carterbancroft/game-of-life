# Conway's Game Of Life in Python 3

## Requirements
Python 3.x

- Pygame: `python3 -m pip install pygame`
- PyYAML: `python3 -m pip install yaml`

## Running the game
From the root of the repository...
```
$ cd python
$ python3 main.py
```

## Running tests
```
$ python3 -m unittest test_world
```
Run individual tests like `python3 -m unittest test_world.GetNeighbors.test_top_left_cell`

## Tweaking it
There are a few config values you can modify to get different, sometimes more interesting, results within this implementation of Life.

**In [config.yml](https://github.com/carterbancroft/game-of-life/blob/master/python/config.yml)**
- `tick_delay` (int) adjusts the amount of time between game ticks. The rules are implemented once during each tick. You'll run up against speed limitations with this on larger worlds.
- `screen_width` / `screen_height` (int) adjusts the size of the world.
- `seed_modifier` (float) increases or decreases the chances of a given cell being alive when the game starts. More cells will be dead in the seed as the number approaches 1 and more will be alive as is approaches 0.

**In [main.py](https://github.com/carterbancroft/game-of-life/blob/master/python/main.py)**
- `cell_color` (pygame color) adjusts the color or the alive cells
