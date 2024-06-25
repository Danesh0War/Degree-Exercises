from copy import deepcopy
from typing import Iterable, List
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from battleship import create_player_board, main, init_board
import helper


class CopyingMock(MagicMock):
    def __call__(self, /, *args, **kwargs):
        args = deepcopy(args)
        kwargs = deepcopy(kwargs)
        return super(CopyingMock, self).__call__(*args, **kwargs)


player_board = [
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

all_board = [f"{letter}{num}" for letter in "ABCDEFGH" for num in range(1, 11)]
all_board_locations = [(num - 1, letter) for letter in range(8) for num in range(1, 11)]


def choose_ship_location_mock(iterable):
    iterator = iter(list(iterable) + ["N"])

    def inner(board, locations):
        return next(iterator)

    return inner


def input_mock(iterable: Iterable):
    iterator = iter(list(iterable) + ["N"])

    def inner(x):
        return next(iterator)

    return inner


def count_strikes(board: List[List[int]]) -> int:
    count = 0
    for row in board:
        for cell in row:
            if cell in [helper.HIT_SHIP, helper.HIT_WATER]:
                count += 1
    return count


class TestMain(TestCase):  # this is the real shit
    def _test_create_player_board(self, mock_create_player_board: Mock):
        mock_create_player_board.assert_called_once_with(
            helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES
        )
        self.assertEqual(
            1,
            mock_create_player_board.call_count,
            "There is one player, you know that?",
        )

    def _test_boards(self, printed_boards):
        self.assertListEqual(
            init_board(helper.NUM_ROWS, helper.NUM_COLUMNS),
            printed_boards[0].args[1],
            "first computer board should clean",
        )
        self.assertListEqual(
            player_board,
            printed_boards[0].args[0],
            "first player board should be mock board",
        )
        for strike_index in range(
            len(printed_boards[:-1])
        ):  # this should apply to all expect the last
            self.assertEqual(
                len(printed_boards[strike_index].args[1]),
                helper.NUM_ROWS,
                "computer board does not have right number of rows",
            )

            # check player strikes at computer board
            if strike_index > 0:
                loc = all_board_locations[strike_index - 1]
                self.assertIn(
                    printed_boards[strike_index].args[1][loc[0]][loc[1]],
                    [helper.HIT_SHIP, helper.HIT_WATER],
                    "chosen target was not strike",
                )
                self.assertIn(
                    printed_boards[strike_index - 1].args[1][loc[0]][loc[1]],
                    [helper.WATER],
                    "showed past location must be water",
                )

                loc = all_board_locations[strike_index - 1]
                self.assertIn(
                    printed_boards[strike_index].args[0][loc[0]][loc[1]],
                    [helper.HIT_SHIP, helper.HIT_WATER],
                    "chosen target was not strike",
                )
                self.assertIn(
                    printed_boards[strike_index - 1].args[0][loc[0]][loc[1]],
                    [helper.WATER, helper.SHIP],
                    "showed past location must be water",
                )

            # check computer generated board
            for row in printed_boards[strike_index].args[1]:
                self.assertEqual(
                    helper.NUM_COLUMNS,
                    len(row),
                    "computer board row does not have wanted number of columns",
                )
                for cell in row:
                    self.assertNotEqual(
                        helper.SHIP,
                        cell,
                        f"computer board should hide the ships, round {strike_index}, row {row}",
                    )

            self.assertEqual(
                strike_index,
                count_strikes(printed_boards[strike_index].args[0]),
                "at each moment the amount of strikes should be equal to the round",
            )
            self.assertEqual(
                strike_index,
                count_strikes(printed_boards[strike_index].args[1]),
                "at each moment the amount of strikes should be equal to the round",
            )

    def _test_should_game_ended(self, printed_boards):
        def _check_board_completion(board: List[List[int]]) -> bool:
            for row in board:
                for column in row:
                    if column == helper.SHIP:
                        return False
            return True

        self.assertTrue(
            _check_board_completion(printed_boards[-1].args[0])
            or _check_board_completion(printed_boards[-1].args[1]),
            "it seems game should not have ended",
        )

    def _test_choose_torpedo_target(self, mock_choose_torpedo_target: Mock):
        all_args = mock_choose_torpedo_target.call_args_list
        for round in range(len(mock_choose_torpedo_target.call_args_list)):
            round_args = all_args[round].args
            self.assertEqual(
                len(round_args[0]),
                helper.NUM_ROWS,
                "please enter board to the torpedo target",
            )
            for row in round_args[0]:
                self.assertEqual(
                    helper.NUM_COLUMNS,
                    len(row),
                    "please enter board to the torpedo target",
                )
                for cell in row:
                    self.assertIn(
                        cell, [0, 1, 2, 3], "please enter board to the torpedo target"
                    )

            self.assertIsInstance(round_args[1], set, "locations should be set")
            self.assertEqual(
                sorted(str(all_board_locations[round:])),
                sorted(str(list(round_args[1]))),
                "you entered invalid locations",
            )

    def setUp(self):
        patcher = patch("helper.print_board", CopyingMock())
        self.mock_print_board = patcher.start()
        self.addCleanup(patcher.stop)

        patcher_mock_choose_torpedo_target = patch(
            "helper.choose_torpedo_target",
            new=CopyingMock(wraps=choose_ship_location_mock(all_board_locations)),
        )
        self.mock_choose_torpedo_target = patcher_mock_choose_torpedo_target.start()
        self.addCleanup(patcher_mock_choose_torpedo_target.stop)

    @patch(
        "battleship.create_player_board", wraps=lambda x, y, z: deepcopy(player_board)
    )
    @patch("helper.get_input", wraps=input_mock(all_board))
    def test_component(
        self,
        mock_get_input: Mock,
        mock_create_player_board: Mock,
    ):
        main()
        printed_boards = self.mock_print_board.call_args_list
        self._test_create_player_board(mock_create_player_board)
        self._test_boards(printed_boards)
        self._test_should_game_ended(printed_boards)
        self.assertEqual(
            len(printed_boards) - 1,
            self.mock_choose_torpedo_target.call_count,
            "amount of board does not exists the amount of time the computer chosed a target",
        )
        self._test_choose_torpedo_target(self.mock_choose_torpedo_target)
