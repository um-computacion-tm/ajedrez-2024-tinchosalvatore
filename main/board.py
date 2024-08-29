from main.rook import Rook
from main.knight import Knight
from main.bishop import Bishop
from main.queen import Queen
from main.king import King
from main.pawn import Pawn
from main.exceptions import *

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
    
    def set_position(self, row, col):
        self.__row__ = row
        self.__col__ = col
        
    # Indica donde esta la pieza
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    # Devuelve el color de la pieza en la posicion indicada
    def get_color(self, row, col):
        piece =  self.get_piece(row, col)
        if piece is None:
            return None
        return piece.get_color()

    # Elimina la pieza en la posicion indicada
    def remove_piece(self, row, col):
        self.__positions__[row][col] = None

    # Metodo para mostrar el tablero
    def show_board(self):
        # Muestra los números de las columnas
        board_representation = "  " + " ".join([str(i) for i in range(8)]) + "\n"

        # Muestra las filas del tablero
        for i, row in enumerate(self.__positions__):
            # Muestra el número de la fila seguido del contenido de la fila
            board_representation += str(i) + " " + " ".join([str(piece) if piece else "." for piece in row]) + "\n"
        return board_representation