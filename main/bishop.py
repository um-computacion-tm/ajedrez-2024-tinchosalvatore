from main.pieces import Piece
from main.movements import ReglasDeMovimientos

class Bishop(Piece):

    #As all pieces will do, bishop heredates from Piece class the color and str method
    #It also calls the diagonal_movement method for the validating move method

    def __init__(self, color):
        super().__init__(color)
        self.__movimientos__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♝"
        else:
            return "♗"
        
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos__.diagonal_move(from_row, from_col, to_row, to_col)
        return True