from main.pieces import Piece
from main.movimientos import ReglasDeMovimientos
from main.exceptions import *

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__movimientos__ = ReglasDeMovimientos()    
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
 
    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Verifica que la torre se mueva en linea horizontal o vertical
        if from_row != to_row and from_col != to_col:
                raise InvalidMoveRook("La torre no se puede mover en diagonal")
        
        if self.__movimientos__.horizontal_move(to_row, to_col) or self.__movimientos__.vertical_move(to_row, to_col):
            return True
