from main.pieces import Piece
from main.movimientos import ReglasDeMovimientos

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__movimientos__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♛"
        else:
            return "♕"
        
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos__.vertical_horizontal_move(from_row, from_col, to_row, to_col) and \
        self.__movimientos__.diagonal_move(from_row, from_col, to_row, to_col)
        return True