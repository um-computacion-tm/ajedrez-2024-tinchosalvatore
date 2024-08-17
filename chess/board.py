from pieces import Piece
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

class Board:
    def __init__(self):
        
        self.__positions__ = self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
            
        self.initialize_board()
            
    def initialize_board(self):
        # Posicion inicial de las piezas negras
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")

        # Posicion inicial de las piezas blancas
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][3] = Queen("WHITE")
        self.__positions__[7][4] = King("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[7][6] = Knight("WHITE")
        self.__positions__[7][7] = Rook("WHITE")
        for i in range(8):
            self.__positions__[6][i] = Pawn("WHITE")
    
    #indica donde esta la pieza
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    #mueve la pieza y detecta si no hay pieza en esa posicion y si el destino esta ocupado
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            return False #ya que no hay pieza en esa posicion
        
        ocupado = self.get_piece(to_row, to_col)
        if ocupado and ocupado.__color__ == piece.__color__:
            return False #ya que hay una pieza en esa posicion

        self.__positions__[from_row][from_col] = None
        self.__positions__[to_row][to_col] = piece
