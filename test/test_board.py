import unittest
from main.board import Board
from main.pawn import Pawn
from main.rook import Rook
from main.knight import Knight
from main.bishop import Bishop
from main.queen import Queen
from main.king import King

class TestBoard(unittest.TestCase):

    def setUp(self):
        """Configuración antes de cada prueba."""
        self.board = Board()

    def test_initial_positions(self):
        """Prueba que las piezas están en las posiciones iniciales correctas."""
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)

    def test_set_piece(self):
        """Prueba que se puede colocar una pieza en el tablero."""
        pawn = Pawn("WHITE")
        self.board.set_piece(pawn, 4, 4)
        self.assertEqual(self.board.get_piece(4, 4), pawn)

    def test_remove_piece(self):
        """Prueba que se puede eliminar una pieza del tablero."""
        self.board.set_piece(None, 4, 4)
        self.board.remove_piece(4, 4)
        self.assertIsNone(self.board.get_piece(4, 4))

    def test_occupied_path_vertical_horizontal(self):
        """Prueba la detección de caminos ocupados en movimientos verticales y horizontales."""
        self.board.set_piece(Rook("WHITE"), 0, 0)
        self.board.set_piece(Pawn("BLACK"), 3, 0)
        self.assertTrue(self.board.occupied_path_vertical_horizontal(0, 0, 7, 0))
        self.assertTrue(self.board.occupied_path_vertical_horizontal(0, 0, 0, 7))
        self.assertFalse(self.board.occupied_path_vertical_horizontal(0, 0, 0, 1))

    def test_occupied_path_diagonal(self):
        """Prueba la detección de caminos ocupados en movimientos diagonales."""
        self.board.set_piece(Bishop("WHITE"), 0, 0)
        self.board.set_piece(Pawn("BLACK"), 2, 2)
        self.assertTrue(self.board.occupied_path_diagonal(0, 0, 7, 7))
        self.assertTrue(self.board.occupied_path_diagonal(0, 0, 2, 2))
        self.assertFalse(self.board.occupied_path_diagonal(0, 0, 1, 2))

    def test_show_board(self):
        """Prueba la representación del tablero."""
        expected_output = (
            "  0 1 2 3 4 5 6 7\n"
            "0 R K B Q K B K R\n"
            "1 P P P P P P P P\n"
            "2 . . . . . . . .\n"
            "3 . . . . . . . .\n"
            "4 . . . . . . . .\n"
            "5 . . . . . . . .\n"
            "6 P P P P P P P P\n"
            "7 R K B Q K B K R\n"
        )
        self.assertEqual(self.board.show_board(), expected_output)

if __name__ == "__main__":
    unittest.main()
