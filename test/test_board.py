import unittest
from main.board import Board
from main.pawn import Pawn
from main.rook import Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initialize_board(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)

    def test_set_piece(self):
        pawn = Pawn("WHITE")
        self.board.set_piece(pawn, 3, 3)
        self.assertEqual(self.board.get_piece(3, 3), pawn)

    def test_get_color(self):
        self.assertEqual(self.board.get_color(0, 0), "BLACK")
        self.assertEqual(self.board.get_color(6, 0), "WHITE")

    def test_remove_piece(self):
        self.board.remove_piece(0, 0)
        self.assertIsNone(self.board.get_piece(0, 0))

    def test_occupied_path_vertical_horizontal(self):
        # Verifica que el camino esté libre inicialmente
        self.assertTrue(self.board.occupied_path_vertical_horizontal(0, 0, 0, 7))
        # Coloca una pieza en el camino y verifica que ahora esté ocupado
        self.assertTrue(self.board.occupied_path_vertical_horizontal(0, 0, 7, 0))


    def test_occupied_path_diagonal(self):
        # Verifica que el camino diagonal esté libre
        self.assertTrue(self.board.occupied_path_diagonal(0, 0, 7, 7))
        # Coloca una pieza en el camino diagonal y verifica que ahora esté ocupado

    def test_get_pawn(self):
        # Crea un peón y colócalo en la posición (1, 1)
        pawn = Pawn("WHITE")
        self.board.set_piece(pawn, 1, 1)
        # Verifica que get_pawn devuelva el peón en la posición (1, 1)
        self.assertEqual(self.board.get_pawn(1, 1), pawn)
        # Verifica que get_pawn devuelva None en una posición sin peón
        self.assertIsNone(self.board.get_pawn(0, 0))
        self.assertIsNone(self.board.get_pawn(2, 2))

    def test_show_board(self):
        expected_output = (
            "  0 1 2 3 4 5 6 7\n"
            "0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 0\n"
            "1 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 1\n"
            "2 . . . . . . . . 2\n"
            "3 . . . . . . . . 3\n"
            "4 . . . . . . . . 4\n"
            "5 . . . . . . . . 5\n"
            "6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 6\n"
            "7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 7\n"
            "  0 1 2 3 4 5 6 7\n"
        )
        
        self.assertEqual(self.board.show_board().strip(), expected_output.strip())
        
if __name__ == "__main__":
    unittest.main()
