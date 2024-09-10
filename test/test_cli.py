import unittest
from unittest.mock import patch, MagicMock
from main.cli import play
from main.chess import Chess

class TestCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=["7", "0", "6", "0"])
    def test_play_move(self, mock_input):
        chess = Chess()
        with patch('main.cli.Chess', return_value=chess):
            play(chess)
        self.assertTrue(chess.is_playing())  # Verifica que el juego sigue en curso tras un movimiento válido

if __name__ == "__main__":
    unittest.main()
