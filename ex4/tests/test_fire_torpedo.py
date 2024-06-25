from unittest import TestCase

from battleship import fire_torpedo
import helper


class TestFireTorpedo(TestCase):
    def test_fire_at_water(self):
        board = [[helper.WATER, helper.HIT_WATER, helper.SHIP, helper.HIT_SHIP]]
        fire_torpedo(board, (0, 1))
        self.assertEqual(board[0][0], helper.WATER)
        self.assertEqual(board[0][1], helper.HIT_WATER)
        self.assertEqual(board[0][2], helper.SHIP)
        self.assertEqual(board[0][3], helper.HIT_SHIP)
        fire_torpedo(board, (0, 0))
        self.assertEqual(board[0][0], helper.HIT_WATER)
        self.assertEqual(board[0][1], helper.HIT_WATER)
        self.assertEqual(board[0][2], helper.SHIP)
        self.assertEqual(board[0][3], helper.HIT_SHIP)

    def test_fire_at_ship(self):
        board = [[helper.WATER, helper.HIT_WATER, helper.SHIP, helper.HIT_SHIP]]
        fire_torpedo(board, (0, 3))
        self.assertEqual(board[0][0], helper.WATER)
        self.assertEqual(board[0][1], helper.HIT_WATER)
        self.assertEqual(board[0][2], helper.SHIP)
        self.assertEqual(board[0][3], helper.HIT_SHIP)
        fire_torpedo(board, (0, 2))
        self.assertEqual(board[0][0], helper.WATER)
        self.assertEqual(board[0][1], helper.HIT_WATER)
        self.assertEqual(board[0][2], helper.HIT_SHIP)
        self.assertEqual(board[0][3], helper.HIT_SHIP)

    def test_fire_outside_board(self):
        same_board = [[helper.WATER, helper.HIT_WATER, helper.SHIP, helper.HIT_SHIP]]
        board = [[helper.WATER, helper.HIT_WATER, helper.SHIP, helper.HIT_SHIP]]
        fire_torpedo(board, (1, 1))
        self.assertListEqual(same_board, board)
