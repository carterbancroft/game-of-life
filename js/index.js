const termkit = require('terminal-kit')
const term = termkit.terminal

const tick_ms = 50
const width = 225
const height = 53
const buffer = new termkit.ScreenBuffer({dst: term, width, height})

const alive = '∎'
const dead = ' '
const dying = 'd'
const being_born = 'b'

function generateWorld() {
  let world = []
  let options = [alive, dead]
  for (let i = 0; i < width; i++) {
    let new_arr = []
    for (let j = 0; j < height; j++) {
      let r = Math.random()
      if (r >= 0.96) r = 0
      else r = 1
      new_arr.push(options[r])
    }
    world.push(new_arr)
  }

  return world
}

function getNeighbors(world, cell_x, cell_y) {
  // Start at the top left corner of our 3x3 grid
  let x = cell_x - 1
  let y = cell_y - 1

  // Use this to keep track of our neighbor values
  const neighbors = []

  for(let i = 0; i < 3; i++) {
    if (x >= width) break

    // If we're off the grid in the x direction, increment y and move on
    if (x < 0) {
      x += 1
      continue
    }

    for (let j = 0; j < 3; j++) {
      if (y >= height) break

      // If we're off the grid in the y direction, increment y and move on
      if (y < 0) {
        y += 1
        continue
      }
      // If we're on the position of the cell we're checking against skip it
      // and move on.
      if (x === cell_x && y === cell_y) {
        y += 1
        continue
      }

      // Hey we found a neighbor, push it's value to the list of neighbors
      neighbors.push(world[x][y])
      y += 1
    }

    // Reset y back to the first column and move down to the next row
    y = cell_y - 1
    x += 1
  }

  return neighbors
}


function determineCellState(neighbors, current_state) {
  // if the current cell is live then...
  //   if it has fewer than 2 lives neighbours it dies
  //   if it has 2 OR 3 live neighbours it remains alive, nothing changes
  //   if it has > 3 live neighbors it dies
  // if the current cell is dead then...
  //   if there are exactly 3 live neighbours then it becomes alive
  //   other wise it stays dead
  //
  let live_neighbors = 0
  let alive_states = [dying, alive]
  neighbors.forEach(n => {
    if (alive_states.includes(n)) live_neighbors += 1
  })
  //console.log(`live_neighbors: ${live_neighbors}, current_state: ${current_state}, ${neighbors}`)

  let new_state = current_state
  // if the cell is currently alive (either dying or truly alive)...
  if (alive_states.includes(current_state)) {
    if (live_neighbors < 2) new_state = dying
    else if (live_neighbors > 3) new_state = dying
  }
  else {
    if (live_neighbors === 3) new_state = being_born
  }

  return new_state
}


function updateWorld(world) {
  for (let i = 0; i < width; i++) {
    for (let j = 0; j < height; j++) {
      let neighbors = getNeighbors(world, i, j)
      let newState = determineCellState(neighbors, world[i][j])
      //console.log(neighbors)
      //console.log(`current = ${world[i][j]}, new = ${newState}`)
      world[i][j] = newState
    }
  }

  // Once we've gone over the whole world and determined all the new states
  // including intermediate states, redraw the whole thing as it should be
  // after this turn.
  for (let i = 0; i < width; i++) {
    for (let j = 0; j < height; j++) {
      if (world[i][j] === dying) world[i][j] = dead // kill it
      else if (world[i][j] === being_born) world[i][j] = alive // bring it to life
    }
  }
}

function printWorld(world) {
  for (let i = 0; i < width; i++) {
    for (let j = 0; j < height; j++) {
      const state = world[i][j]
      let color = 'black'
      if (state === alive) color = 'green'
      buffer.put({x: i, y: j, attr: {color}}, state)
    }
  }
  buffer.draw()
}

let world = generateWorld()
//printWorld(world)

function run() {
  setTimeout(() => {
    updateWorld(world)
    printWorld(world)
    run();
  }, tick_ms)
}

run();

