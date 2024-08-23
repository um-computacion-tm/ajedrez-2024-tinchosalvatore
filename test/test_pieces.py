import unittest
from main.pieces import Piece

class TestPiece(unittest.TestCase):

    def test_initial_color(self): #testea get_color
        piece = Piece("WHITE")
        self.assertEqual(piece.get_color(), "WHITE")

    def test_set_position(self): #testea set_position
        piece = Piece("BLACK")
        piece.set_position(3, 3)
        self.assertEqual(piece.__position__, (3, 3))

if __name__ == '__main__':
    unittest.main()