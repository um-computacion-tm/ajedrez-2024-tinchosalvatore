from main.pieces import Piece
from main.movements import ReglasDeMovimientos

#King heredates from Piece class the color and str method and calls the king_movement method for the validating move method

class King(Piece):
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♚"
        else:
            return "♔"
    
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos_king__.king_movement(from_row, from_col, to_row, to_col)
        return True

    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_king__ = ReglasDeMovimientos()