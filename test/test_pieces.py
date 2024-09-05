import unittest
from main.pawn import Pawn
from main.rook import Rook
from main.knight import Knight
from main.bishop import Bishop
from main.queen import Queen
from main.king import King
from main.exceptions import InvalidMovePawn, InvalidMoveVerticalHorizontal, InvalidMoveDiagonal, InvalidMoveKnight, InvalidMoveKing

class TestChessPieces(unittest.TestCase):

    def test_pawn_moves(self):
        white_pawn = Pawn("WHITE")
        black_pawn = Pawn("BLACK")
        
        # Movimiento válido de un paso hacia adelante
        self.assertTrue(white_pawn.valid_moves_pawn(6, 0, 5, 0))
        self.assertTrue(black_pawn.valid_moves_pawn(1, 0, 2, 0))
        
        # Movimiento inicial de dos pasos
        self.assertTrue(white_pawn.valid_moves_pawn(6, 0, 4, 0))
        self.assertTrue(black_pawn.valid_moves_pawn(1, 0, 3, 0))
        
        # Movimiento inválido
        with self.assertRaises(InvalidMovePawn):
            white_pawn.valid_moves_pawn(6, 0, 3, 0)
    
    def test_rook_moves(self):
        rook = Rook("WHITE")
        
        # Movimiento válido en vertical y horizontal
        self.assertTrue(rook.valid_moves(0, 0, 0, 5))  # Movimiento horizontal
        self.assertTrue(rook.valid_moves(0, 0, 5, 0))  # Movimiento vertical
        
        # Movimiento inválido (diagonal)
        with self.assertRaises(InvalidMoveVerticalHorizontal):
            rook.valid_moves(0, 0, 5, 5)
    
    def test_knight_moves(self):
        knight = Knight("WHITE")
        
        # Movimiento válido en forma de L
        self.assertTrue(knight.valid_moves(0, 1, 2, 2))
        self.assertTrue(knight.valid_moves(0, 1, 2, 0))
        
        # Movimiento inválido
        with self.assertRaises(InvalidMoveKnight):
            knight.valid_moves(0, 1, 3, 3)
    
    def test_bishop_moves(self):
        bishop = Bishop("WHITE")
        
        # Movimiento válido en diagonal
        self.assertTrue(bishop.valid_moves(0, 2, 2, 4))
        self.assertTrue(bishop.valid_moves(0, 2, 3, 5))
        
        # Movimiento inválido (no diagonal)
        with self.assertRaises(InvalidMoveDiagonal):
            bishop.valid_moves(0, 2, 2, 3)
    
    def test_queen_moves(self):
        queen = Queen("WHITE")
        
        # Movimiento válido en vertical, horizontal y diagonal
        self.assertTrue(queen.valid_moves(0, 3, 0, 7))  # Horizontal
        self.assertTrue(queen.valid_moves(0, 3, 4, 3))  # Vertical
        self.assertTrue(queen.valid_moves(0, 3, 4, 7))  # Diagonal
        
        # Movimiento inválido
        with self.assertRaises(InvalidMoveDiagonal):
            queen.valid_moves(0, 3, 5, 6)
    
    def test_king_moves(self):
        king = King("WHITE")
        
        # Movimiento válido de una casilla en cualquier dirección
        self.assertTrue(king.valid_moves(0, 4, 1, 4))  # Vertical
        self.assertTrue(king.valid_moves(0, 4, 0, 5))  # Horizontal
        self.assertTrue(king.valid_moves(0, 4, 1, 5))  # Diagonal
        
        # Movimiento inválido (más de una casilla)
        with self.assertRaises(InvalidMoveKing):
            king.valid_moves(0, 4, 2, 4)

if __name__ == '__main__':
    unittest.main()
