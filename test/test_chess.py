import unittest
from main.pawn import Pawn
from main.king import King
from main.exceptions import *
from main.chess import Chess

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
        self.board = self.chess.get_board()  # Accede al tablero privado para configurar el estado inicial

    def test_turn_initial(self):
        self.assertEqual(self.chess.turn(), "WHITE")

    def test_piece(self):
        # Asume que hay una pieza en la posición (0, 0)
        piece = self.chess.piece(0, 0)
        self.assertIsNotNone(piece)

    def test_target_piece(self):
        # Asume que hay una pieza en la posición (0, 0)
        target_piece = self.chess.target_piece(0, 0)
        self.assertIsNotNone(target_piece)

    def test_capture_piece(self):
        # Prepara un escenario para captura
        self.board.set_piece(Pawn("BLACK"), 1, 1)
        self.board.set_piece(Pawn("WHITE"), 2, 1)

        # Verifica que se capture la pieza enemiga
        result = self.chess.capture_piece(2, 1, 1, 1)
        self.assertTrue(result)
        self.assertIsNone(self.board.get_piece(2, 1))  # Asegura que la pieza enemiga fue removida


    def test_capture_success(self):
        """ Test capturing a piece of the opposite color. """
        self.chess.capture_piece(0, 0, 1, 0)  # La torre blanca captura el peón negro
        self.assertTrue
        self.assertIsNone(self.chess.capture_piece(2, 0, 3, 0))
        self.assertFalse(self.chess.capture_piece(0, 0, 2, 0))
        # I set the king in a place where I can test what happens if he was captured
        self.board.set_piece(King("WHITE"), 0, 0)


    def test_pawn_capture(self):
        # Prepara un escenario para captura de peón
        self.board.set_piece(Pawn("WHITE"), 1, 1)
        self.board.set_piece(Pawn("BLACK"), 2, 2)

        # Ejecuta el movimiento de captura
        self.chess.pawn_capture(1, 1, 2, 2)
        self.assertTrue
        self.assertIsNone(self.board.get_piece(4, 4))

    def test_pieces_movements_changes_turn(self):
        # Prepara un escenario para captura de peón
        self.board.set_piece(Pawn("WHITE"), 6, 0)
        self.board.set_piece(Pawn("BLACK"), 5, 1)
        # Ejecuta el movimiento de captura
        self.chess.pieces_movements(6, 0, 5, 1)

        # Verifica si el turno ha cambiado
        self.assertEqual(self.chess.turn(), "BLACK")

    def test_pawn_invalid_move_to_occupied_square(self):
        # Prepara un escenario donde el peón intenta moverse a una casilla ocupada
        self.board.set_piece(Pawn("WHITE"), 6, 0)
        self.board.set_piece(Pawn("WHITE"), 5, 0)  # Peón blanco en el destino

        # Verifica que se lanza la excepción de movimiento inválido
        with self.assertRaises(InvalidMoveNotAllowed):
            self.chess.pieces_movements(6, 0, 5, 0)

    def pieces_movements(self):
        self.chess.move_piece(6, 0, 5, 0)
        self.assertTrue

    def test_ocuppied_path(self):
        # Prepara el escenario
        self.board.set_piece(Pawn("WHITE"), 0, 0)
        self.board.set_piece(Pawn("BLACK"), 1, 0)
        self.assertTrue(self.chess.ocuppied_path(0, 0, 2, 0))


    def test_move_piece(self):
        # Mover un peón blanco hacia adelante
        self.chess.move_piece(6, 0, 5, 0)

    def test_move_piece_same_color(self):
        with self.assertRaises(InvalidMoveSameColor):
            self.chess.turn = "WHITE"
            self.chess.move_piece(7, 0, 6, 0)

    def test_move_piece_no_piece(self):
        with self.assertRaises(InvalidMoveNoPiece):
            self.chess.move_piece(4, 0, 3, 0)
        
    def test_move_piece_path_blocked(self):
        self.board.set_piece(Pawn("WHITE"), 6, 0)
        self.board.set_piece(Pawn("BLACK"), 5, 0)  # Peón negro bloqueando el camino

        with self.assertRaises(InvalidMovePathOcuppied):
            self.chess.move_piece(6, 0, 4, 0)

    def test_move_pawn_capture_diagonal(self):
        self.board.set_piece(Pawn("BLACK"), 1, 1)
        self.board.set_piece(Pawn("WHITE"), 2, 2)

        self.chess.move_piece(2, 2, 1, 1)
        self.assertIsNone(self.board.get_piece(2, 2))  # Asegura que la pieza negra fue capturada
        self.assertIsNotNone(self.board.get_piece(1, 1))  # Verifica que el peón blanco se movió



    def test_invalid_move_pawn(self):
        with self.assertRaises(InvalidMoveNotAllowed):
            self.chess.move_piece(6, 0, 5, 1)
    
    def test_invalid_move_piece_from_other_color(self):
        with self.assertRaises(InvalidMovePieceFromOtherColor):
            self.chess.move_piece(1, 0, 3, 0)

    def test_pawn_capture(self):
        # Prepara un escenario para captura de peón
        self.board.set_piece(Pawn("WHITE"), 1, 1)
        self.board.set_piece(Pawn("BLACK"), 2, 2)

        # Ejecuta el movimiento de captura
        self.chess.pawn_capture(1, 1, 2, 2)

        
    def test_king_dead(self):
        self.board.set_piece(King("WHITE"), 0, 0)
        self.assertTrue(self.chess.king_dead(0, 0))
        self.assertFalse(self.chess.king_dead(1, 0))

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
        
        self.assertEqual(self.chess.show_board().strip(), expected_output.strip())

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())
        self.chess.end_game()
        self.assertFalse(self.chess.is_playing())


if __name__ == "__main__":
    unittest.main()