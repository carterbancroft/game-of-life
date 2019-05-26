import unittest
import world_helper

class TestAddition(unittest.TestCase):
    def test_addition(self):
        print('In unit test')
        answer = life.test(5, 6)
        self.assertEqual(answer, 11)
