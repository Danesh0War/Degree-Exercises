from unittest import TestCase

from battleship import init_board


class TestInitBoard(TestCase):
    def test_sizes(self):
        board = init_board(5, 10)
        self.assertEqual(5, len(board), "rows length is invalid")
        for row in board:
            self.assertEqual(10, len(row), f"column length is invalid in row {row}")

    def test_different_instances(self):
        board = init_board(7, 3)
        for row_index in range(len(board)):
            test_column = board[row_index]
            for column in board[row_index + 1 :]:
                self.assertIsNot(
                    test_column, column, f"two columns are of the same instance, row: {row_index}"
                )