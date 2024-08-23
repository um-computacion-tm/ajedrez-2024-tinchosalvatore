import unittest
from main.board import Board
from main.rook import Rook
from main.exceptions import *

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()

    def test_initial_setup(self):
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertIsNone(self.__board__.get_piece(4, 4))

    def test_get_color(self):
        self.assertEqual(self.__board__.get_color(0, 0), "BLACK")
        self.assertEqual(self.__board__.get_color(7, 7), "WHITE")
        self.assertIsNone(self.__board__.get_color(4, 4))

    def test_move_piece_successful(self):
        self.__board__.move_piece(6, 0, 5, 0)
        self.assertIsNone(self.__board__.get_piece(6, 0))
        self.assertIsNotNone(self.__board__.get_piece(5, 0))

    def test_move_piece_invalid_same_color(self):
        with self.assertRaises(InvalidMoveSameColor):
            self.__board__.move_piece(7, 0, 7, 1)

    def test_capture_piece(self):
        self.__board__.move_piece(6, 0, 5, 0) # Mueve los peones 
        self.__board__.move_piece(1, 0, 2, 0)
        self.assertTrue(self.__board__.capture_piece(5, 0, 2, 0))  # El peon blanco captura el peon negro

if __name__ == '__main__':
    unittest.main()
