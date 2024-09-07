import unittest
from main.chess import Chess
from main.exceptions import InvalidMoveNoPiece

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_turn(self):
        self.assertEqual(self.chess.turn(), "WHITE")

    def test_capture_piece(self):
        with self.assertRaises(InvalidMoveNoPiece):
            self.chess.capture_piece(5, 0, 4, 0)

    def test_move_piece(self):
        with self.assertRaises(InvalidMoveNoPiece):
            self.chess.move_piece(5, 0, 4, 0)

    def test_king_dead(self):
        self.assertFalse(self.chess.king_dead(7, 4))  # Asume que el rey no está muerto al inicio

if __name__ == "__main__":
    unittest.main()
