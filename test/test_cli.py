import unittest
from unittest.mock import patch, MagicMock
from main.chess import Chess
from main.exceptions import InvalidInput, InvalidMove
import io
import os
import sys

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()
        self.chess.show_board = MagicMock(return_value="Tablero")
        self.chess.turn = MagicMock(return_value="Blancas")
        self.chess.move_piece = MagicMock()
        self.chess.end_game = MagicMock()
    
    def test_invalid_row_input(self):
        with patch('builtins.input', side_effect=['8', '1', '1', '1']):
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                from main.cli import play
                play(self.chess)
                output = fake_out.getvalue()
                self.assertIn("Las posiciones deben estar entre 0 y 7.", output)

    def test_non_numeric_input(self):
      with patch('builtins.input', side_effect=['a', '1', '1', '1']):
          with patch('sys.stdout', new=io.StringIO()) as fake_out:
              from main.cli import play
              play(self.chess)
              output = fake_out.getvalue()
              self.assertIn("Ingrese numeros", output)

    def test_move_piece_invalid(self):
        self.chess.move_piece.side_effect = InvalidMove("Movimiento inválido")
        with patch('builtins.input', side_effect=['1', '1', '2', '2']):
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                from main.cli import play
                play(self.chess)
                output = fake_out.getvalue()
                self.assertIn("Movimiento inválido", output)

    def test_exit_command(self):
        with patch('builtins.input', side_effect=['exit']):
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                from main.cli import play
                play(self.chess)
                self.chess.end_game.assert_called_once()
                output = fake_out.getvalue()
                self.assertIn("El usuario terminó el juego.", output)

    def test_valid_move(self):
        with patch('builtins.input', side_effect=['1', '1', '2', '2']):
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                from main.cli import play
                play(self.chess)
                self.chess.move_piece.assert_called_with(1, 1, 2, 2)
                output = fake_out.getvalue()
                self.assertIn("Tablero", output)

if __name__ == '__main__':
    unittest.main()