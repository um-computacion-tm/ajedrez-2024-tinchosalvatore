from main.pieces import Piece
from main.movements import ReglasDeMovimientos

# Rook heredates from Piece class the color and str method and calls the vertical_horizontal_move method for the validating move method

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_rook__ = ReglasDeMovimientos()    
    
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos_rook__.vertical_horizontal_move(from_row, from_col, to_row, to_col)
        return True

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"