from main.pieces import Piece
from main.movements import ReglasDeMovimientos

class Knight(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self.__movimientos__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♞"
        else:
            return "♘"
        
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos__.knight_movement(from_row, from_col, to_row, to_col)
        return True