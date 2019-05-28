# Conway's Game Of Life in JavaScript
This version isn't fleshed out as much as my Python version but it works about the same.

## Requirements
[Node.js](https://nodejs.org/en/download/)

I realize Node is a little heavy handed but it made it simple to get a terminal graphics package that was easy to use and rendered cells quickly.

## Setting up and running the game
From the root of this repository...
```
$ cd js
$ npm install
$ node index.js
```
`ctrl+c` to exit

## Running tests
There are no tests. Don't judge me. Maybe I'll add some at some point.

## Tweaking it
There are a few variables you can modify to get different, sometimes more interesting, results within this implementation of Life.

**In [index.js](https://github.com/carterbancroft/game-of-life/blob/master/js/index.js)**
- `tick_ms` (int) adjusts the amount of time between game ticks. The rules are implemented once during each tick.
- `width` / `height` (int) adjusts the size of the world.
- `color` (string) A little more buried but just search the file for it. Adjusts the color of living cells.
- `life_threshold` (float) increases or decreases the chances of a given cell being alive when the game starts. More cells will be dead in the seed as the number approaches 1 and more will be alive as is approaches 0.
