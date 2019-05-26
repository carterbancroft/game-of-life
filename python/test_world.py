# 3rd party
import unittest

# Package level
import world

# Note that I'm not using cell_states here... If I change a state value that
# could break all these tests. However I think the current way reads better.
# Leaving it as is for now.

class GetNeighbors(unittest.TestCase):
    def test_center_cell_surrounded_by_dead(self):
        world = [
            ['.', '.', '.'],
            ['.', 'a', '.'],
            ['.', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        expected = ['.', '.', '.', '.', '.', '.', '.', '.']

        self.assertEqual(neighbors, expected)

    def test_center_cell_some_alive(self):
        world = [
            ['a', '.', 'a'],
            ['.', 'a', '.'],
            ['a', 'a', 'a'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        expected = ['a', '.', 'a', '.', '.', 'a', 'a', 'a']

        self.assertEqual(neighbors, expected)

    def test_top_left_cell(self):
        world = [
            ['.', 'a', '.'],
            ['a', 'a', '.'],
            ['.', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 0, 0)
        expected = ['a', 'a', 'a']

        self.assertEqual(neighbors, expected)

    def test_top_right_cell(self):
        world = [
            ['a', '.', 'a'],
            ['a', '.', '.'],
            ['a', 'a', 'a'],
        ]

        neighbors = world_helper.getNeighbors(world, 0, 2)
        expected = ['.', '.', '.']

        self.assertEqual(neighbors, expected)

    def test_bottom_left_cell(self):
        world = [
            ['.', '.', '.'],
            ['a', 'a', '.'],
            ['.', 'a', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 2, 0)
        expected = ['a', 'a', 'a']

        self.assertEqual(neighbors, expected)

    def test_bottom_right_cell(self):
        world = [
            ['a', 'a', 'a'],
            ['a', '.', '.'],
            ['a', '.', 'a'],
        ]

        neighbors = world_helper.getNeighbors(world, 2, 2)
        expected = ['.', '.', '.']

        self.assertEqual(neighbors, expected)


class DetermineCellState(unittest.TestCase):
    def test_currently_alive_no_alive_neighbors(self):
        world = [
            ['.', '.', '.'],
            ['.', 'a', '.'],
            ['.', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, 'a')

        self.assertEqual(new_state, 'd')

    def test_currently_alive_one_alive_neighbor(self):
        world = [
            ['a', '.', '.'],
            ['.', 'a', '.'],
            ['.', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, 'a')

        self.assertEqual(new_state, 'd')

    def test_currently_alive_two_alive_neighbors(self):
        world = [
            ['a', '.', '.'],
            ['.', 'a', 'a'],
            ['.', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, 'a')

        self.assertEqual(new_state, 'a')

    def test_currently_alive_three_alive_neighbors(self):
        world = [
            ['a', '.', '.'],
            ['.', 'a', 'a'],
            ['a', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, 'a')

        self.assertEqual(new_state, 'a')

    def test_currently_alive_four_alive_neighbors(self):
        world = [
            ['a', '.', '.'],
            ['.', 'a', 'a'],
            ['a', 'a', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, 'a')

        self.assertEqual(new_state, 'd')

    def test_currently_dead_one_alive_neighbor(self):
        world = [
            ['a', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, '.')

        self.assertEqual(new_state, '.')

    def test_currently_dead_two_alive_neighbors(self):
        world = [
            ['a', '.', '.'],
            ['.', '.', '.'],
            ['.', 'a', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, '.')

        self.assertEqual(new_state, '.')

    def test_currently_dead_three_alive_neighbors(self):
        world = [
            ['a', '.', '.'],
            ['.', '.', 'a'],
            ['.', 'a', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, '.')

        self.assertEqual(new_state, 'b')

    def test_currently_dead_four_alive_neighbors(self):
        world = [
            ['a', '.', '.'],
            ['.', '.', 'a'],
            ['a', 'a', '.'],
        ]

        neighbors = world_helper.getNeighbors(world, 1, 1)
        new_state = world_helper.determineCellState(neighbors, '.')

        self.assertEqual(new_state, '.')

class UpdateWorld(unittest.TestCase):
    def test_block(self):
        world = [
            ['.', '.', '.'],
            ['.', 'a', 'a'],
            ['.', 'a', 'a'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['.', '.', '.'],
            ['.', 'a', 'a'],
            ['.', 'a', 'a'],
        ]

        self.assertEqual(world, expected)

    def test_tub(self):
        world = [
            ['.', 'a', '.'],
            ['a', '.', 'a'],
            ['.', 'a', '.'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['.', 'a', '.'],
            ['a', '.', 'a'],
            ['.', 'a', '.'],
        ]

        self.assertEqual(world, expected)

    def test_blinker(self):
        world = [
            ['.', '.', '.'],
            ['a', 'a', 'a'],
            ['.', '.', '.'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['.', 'a', '.'],
            ['.', 'a', '.'],
            ['.', 'a', '.'],
        ]

        self.assertEqual(world, expected)

    def test_beacon(self):
        world = [
            ['a', 'a', '.', '.'],
            ['a', 'a', '.', '.'],
            ['.', '.', 'a', 'a'],
            ['.', '.', 'a', 'a'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['a', 'a', '.', '.'],
            ['a', '.', '.', '.'],
            ['.', '.', '.', 'a'],
            ['.', '.', 'a', 'a'],
        ]

        self.assertEqual(world, expected)

    def test_beacon_2(self):
        world = [
            ['a', 'a', '.', '.'],
            ['a', '.', '.', '.'],
            ['.', '.', '.', 'a'],
            ['.', '.', 'a', 'a'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['a', 'a', '.', '.'],
            ['a', 'a', '.', '.'],
            ['.', '.', 'a', 'a'],
            ['.', '.', 'a', 'a'],
        ]

        self.assertEqual(world, expected)

    def test_glider(self):
        world = [
            ['.', '.', '.', '.', '.'],
            ['.', '.', 'a', '.', '.'],
            ['a', '.', 'a', '.', '.'],
            ['.', 'a', 'a', '.', '.'],
            ['.', '.', '.', '.', '.'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['.', '.', '.', '.', '.'],
            ['.', 'a', '.', '.', '.'],
            ['.', '.', 'a', 'a', '.'],
            ['.', 'a', 'a', '.', '.'],
            ['.', '.', '.', '.', '.'],
        ]

        self.assertEqual(world, expected)

    def test_glider_2(self):
        world = [
            ['.', '.', '.', '.', '.'],
            ['.', 'a', '.', '.', '.'],
            ['.', '.', 'a', 'a', '.'],
            ['.', 'a', 'a', '.', '.'],
            ['.', '.', '.', '.', '.'],
        ]

        world_helper.updateWorld(world)

        expected = [
            ['.', '.', '.', '.', '.'],
            ['.', '.', 'a', '.', '.'],
            ['.', '.', '.', 'a', '.'],
            ['.', 'a', 'a', 'a', '.'],
            ['.', '.', '.', '.', '.'],
        ]

        self.assertEqual(world, expected)
