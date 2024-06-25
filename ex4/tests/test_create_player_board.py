from datetime import datetime
from itertools import zip_longest
import time
from unittest import TestCase
from unittest.mock import Mock, patch, call

from battleship import create_player_board, init_board


def first_input_generator():
    yield "A1"
    yield "B2"
    yield "C3"


def second_input_generator():
    yield "A1"
    yield "F8"  # invalid
    yield "B2"
    yield "F8"  # invalid
    yield "F8"  # invalid
    yield "C3"


global input_calls, print_calls, inputs_calls_values


def input_mock(input_generator):
    generator = input_generator()

    def inner(x):
        time.sleep(0.1)
        input_calls[datetime.now()] = x
        inputs_calls_values.append(x)
        return next(generator)

    return inner


def print_mock():
    def inner(x):
        time.sleep(0.1)
        print_calls[datetime.now()] = x
        time.sleep(0.1)
        return

    return inner


class TestCreatePlayerBoard(TestCase):
    def test_create_empty_board(self):
        expected_board = init_board(5, 5)
        self.assertListEqual(expected_board, create_player_board(5, 5, []))

    def setUp(self):
        global input_calls
        global print_calls
        global inputs_calls_values
        input_calls = {}
        print_calls = {}
        inputs_calls_values = []

    @patch("helper.get_input", wraps=input_mock(first_input_generator))
    @patch("helper.print_board", wraps=print_mock())
    def test_create_board_only_with_valid_placings(
        self, mock_get_input: Mock, mock_print_board: Mock
    ):
        expected_board = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
        self.assertListEqual(expected_board, create_player_board(3, 3, [3, 2, 1]))
        self.assertEqual(3, mock_get_input.call_count)
        self.assertEqual(3, mock_print_board.call_count)
        for print, input in zip_longest(print_calls.keys(), input_calls.keys()):
            self.assertGreater(
                input,
                print,
                "input must be called after print, i think correct me if i am incorrect",
            )

    @patch("helper.get_input", wraps=input_mock(second_input_generator))
    @patch("helper.print_board", wraps=print_mock())
    def test_board_with_some_invalid_placings(
        self, mock_get_input: Mock, mock_print_board: Mock
    ):
        expected_board = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
        board = create_player_board(3, 3, [3, 2, 1])

        self.assertEqual(6, mock_get_input.call_count)
        self.assertEqual(6, mock_print_board.call_count)
        self.assertEqual(6, len(inputs_calls_values))
        self.assertListEqual(expected_board, board)
        self.assertNotEqual(
            inputs_calls_values[0],
            inputs_calls_values[2],
            "retry input message must be different",
        )
        self.assertNotEqual(
            inputs_calls_values[0],
            inputs_calls_values[4],
            "retry input message must be different",
        )
        self.assertEqual(
            inputs_calls_values[5],
            inputs_calls_values[4],
            "retry input message must be different",
        )
        for print, input in zip_longest(print_calls.keys(), input_calls.keys()):
            self.assertGreater(
                input,
                print,
                "input must be called after print, i think correct me if i am incorrect",
            )
