from main.pieces import Piece
from main.movements import ReglasDeMovimientos

#Knight heredates from Piece class the color and str method and calls the knight_movement method for the validating move method

class Knight(Piece):
    
    def __init__(self, color):
        super().__init__(color)
        self.__movimientos_knight__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♞"
        else:
            return "♘"
        
    def valid_moves(self, from_row, from_col, to_row, to_col):
        self.__movimientos_knight__.knight_movement(from_row, from_col, to_row, to_col)
        return True