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
    
    # Indica donde esta la pieza
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    # Devuelve el color de la pieza en la posicion indicada
    def get_color(self, row, col):
        return self.__positions__[row][col].get_color()

    # Elimina la pieza en la posicion indicada
    def remove_piece(self, row, col):
        self.__positions__[row][col] = None

    # Captura la pieza en la posicion indicada
    def capture_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            return None  # No piece at the start position

        target_piece = self.get_piece(to_row, to_col)
        if target_piece and target_piece.get_color() != piece.get_color():
            self.remove_piece(to_row, to_col)  # Remove the captured piece
            self.__positions__[from_row][from_col] = None
            self.__positions__[to_row][to_col] = piece
            piece.set_position(to_row, to_col)
            return True
        return False

    # Mueve la pieza y detecta si no hay pieza en esa posicion y si el destino esta ocupado
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        
        if piece is None:
            return None # Ya que no hay pieza en esa posicion
        
        target_piece = self.get_piece(to_row, to_col)
        if target_piece and target_piece.get_color() == piece.get_color():
            return False  # Pieza en el destino es del mismo color

        if self.capture_piece(from_row, from_col, to_row, to_col):
            return True  # Pieza en el destino es del enemigo y se captura
        
        
        self.__positions__[from_row][from_col] = None
        self.__positions__[to_row][to_col] = piece
        piece.set_position(to_row, to_col)

    
    def show_board(self):
        board_representation = ""
        for row in self.__positions__:
            board_representation += " ".join([str(piece) if piece else "." for piece in row]) + "\n"
        return board_representation