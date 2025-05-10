import unittest
from game_files.game import Game

test_board = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 4, 4]]

cell_size = 50


class TestGame(unittest.TestCase):
    def setUp(self):
        self.test_game = Game(test_board, cell_size)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_correct_place(self):
        test_highlight = self.test_game.highlight
        self.assert_coordinates_equal(test_highlight, 0, 0)

        self.test_game.move_highlight(dy=+cell_size)
        self.assert_coordinates_equal(test_highlight, 0, cell_size)

        self.test_game.move_highlight(dx=-cell_size)
        self.assert_coordinates_equal(test_highlight, 0, cell_size)

        self.test_game.move_highlight(dx=+3*cell_size)
        self.assert_coordinates_equal(test_highlight, 3*cell_size, cell_size)
