from main.pieces import Piece
from main.movements import ReglasDeMovimientos

#Queen heredates from Piece class the color and str method and calls the queen_movement method for the validating move method

class Queen(Piece):
    
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos_queen__.queen_movement(from_row, from_col, to_row, to_col)
        return True

    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_queen__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♛"
        else:
            return "♕"