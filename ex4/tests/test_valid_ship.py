from unittest import TestCase

from battleship import valid_ship, init_board
import helper


class TestValidShip(TestCase):
    def test_empty_board(self):
        board = init_board(3, 3)
        self.assertFalse(
            valid_ship(board, 4, (0, 0)), "dont allow to place too long board"
        )
        self.assertFalse(
            valid_ship(board, 1, (4, 2)), "dont allow to place row outside of the board"
        )
        self.assertFalse(
            valid_ship(board, 1, (2, 4)),
            "dont allow to place column outside of the board",
        )
        self.assertTrue(valid_ship(board, 1, (2, 2)))
        self.assertTrue(valid_ship(board, 3, (0, 2)))
        self.assertTrue(valid_ship(board, 2, (1, 1)))

    def test_placing_near_other_ships(self):
        board = init_board(3, 3)
        board[1][1] = helper.SHIP

        self.assertTrue(valid_ship(board, 3, (0, 0)))
        self.assertTrue(valid_ship(board, 3, (0, 2)))
        self.assertTrue(valid_ship(board, 1, (0, 1)))
        self.assertTrue(valid_ship(board, 1, (2, 1)))

        self.assertFalse(
            valid_ship(board, 3, (0, 1)), "cant place a ship on another ship"
        )
        self.assertFalse(
            valid_ship(board, 1, (1, 1)), "cant place a ship on another ship"
        )
