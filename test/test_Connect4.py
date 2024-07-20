import unittest
from src.connect4.Connect4 import *


class TestConnect4(unittest.TestCase):
    def setUp(self) -> None:
        self._connect4 = Connect4()
        self._ref_array = [[0 for _ in range(6)] for _ in range(7)]

    def test_play(self):
        self._ref_array[0][0] = 1
        self._connect4.play(0)
        self.assertEqual(self._ref_array, self._connect4.get_grid())
        self.assertRaises(ValueError, self._connect4.play, -1)
        self.assertRaises(ValueError, self._connect4.play, 7)
        for _ in range(6):
            self._connect4.play(2)
        self.assertRaises(ValueError, self._connect4.play, 2)

    def test_str(self):
        self.assertEqual(str(self._connect4), (('0'*7) + '\n')*6)
        self._connect4.play(1)
        self.assertEqual(str(self._connect4), (('0'*7)+'\n')*5 + '0100000')

    def test_is_finished(self):
        self.assertEqual(self._connect4.is_finished(), False)
        for i in range(4):
            self._ref_array[0][i] = 1
        self.assertEqual(self._connect4.is_finished(), True)


if __name__ == '__main__':
    unittest.main()
