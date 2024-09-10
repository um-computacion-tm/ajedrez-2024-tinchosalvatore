import unittest
from main.chess import Chess
from main.exceptions import InvalidMoveNoPiece

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_turn(self):
        self.assertEqual(self.chess.turn(), "WHITE")

    def test_capture_success(self):
        """ Test capturing a piece of the opposite color. """
        self.chess.capture_piece(0, 0, 1, 0)  # La torre blanca captura el peón negro
        self.assertTrue

    def test_move_piece(self):
        # Mover un peón blanco hacia adelante
        self.chess.move_piece(6, 0, 5, 0)
        # Intentar mover una pieza desde una posición vacía debe fallar
        with self.assertRaises(InvalidMoveNoPiece):
            self.chess.move_piece(6, 0, 5, 0)

if __name__ == "__main__":
    unittest.main()