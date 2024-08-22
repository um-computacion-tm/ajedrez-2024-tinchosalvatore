import unittest
from chess import Chess
from board import Board
from exceptions import *

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess() # instancia de chess para no tener que instanciarlo en cada test

    def test_initial_turn(self): # testea que inicie con turno de blanco
        self.assertEqual(self.chess.turn(), "WHITE") 
    
    def test_change_turn(self): # testea los cambios de turno
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(), "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(), "WHITE")

    def test_move_successful(self):
        self.chess.move(6, 0, 5, 0)  # Move white pawn forward
        self.assertEqual(self.chess.turn(), "BLACK")


    def test_move_invalid_no_piece(self):
        with self.assertRaises(InvalidMoveNoPiece):
            self.chess.move(4, 4, 3, 3) 

    def test_move_invalid_piece_from_other_color(self):
        with self.assertRaises(InvalidMovePieceFromOtherColor):
            self.chess.move(1, 0, 2, 0)

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())

if __name__ == '__main__':
    unittest.main()
