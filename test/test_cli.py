import unittest
from main.chess import Chess
from main.exceptions import InvalidInput, InvalidMove

class TestChessCLI(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()

    def test_game_starts_correctly(self):
        self.assertTrue(self.chess.is_playing())
        self.assertIsNotNone(self.chess.show_board())
        self.assertIn(self.chess.turn(), ['white', 'black'])

    def test_input_exit(self):
        # Simulate user input for 'exit'
        self.chess.end_game()
        self.assertFalse(self.chess.is_playing())

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(InvalidInput):
            self.chess.move_piece("a", 1, 2, 3)  # Invalid input type (str instead of int)

    def test_invalid_input_partial_numeric(self):
        with self.assertRaises(InvalidInput):
            self.chess.move_piece(1, "b", 2, 3)  # Invalid input type

    def test_invalid_move(self):
        # Assuming that move (0, 0) to (1, 0) is invalid at the start of the game
        with self.assertRaises(InvalidMove):
            self.chess.move_piece(0, 0, 1, 0)

    def test_valid_move(self):
        # Assuming that a valid move is moving a pawn from (1, 0) to (2, 0)
        try:
            self.chess.move_piece(1, 0, 2, 0)
        except InvalidMove:
            self.fail("move_piece() raised InvalidMove unexpectedly!")

if __name__ == '__main__':
    unittest.main()
