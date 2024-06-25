from unittest import TestCase

from battleship import cell_loc


class TestCellLoc(TestCase):
    def test_valid_inputs(self):
        self.assertEqual((1, 0), cell_loc("A2"))
        self.assertEqual((1, 5), cell_loc("F2"))
        XNS = [f"{letter}{num}" for letter in "ABCDEFGH" for num in range(1, 11)]
        locs = [(num - 1, letter) for letter in range(8) for num in range(1, 11)]
        for xn, loc in zip(XNS, locs):
            self.assertEqual(loc, cell_loc(xn), f"{xn} should be {loc}")
