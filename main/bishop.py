from main.pieces import Piece
from main.exceptions import *

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♝"
        else:
            return "♗"
    
    def is_valid_move(self, to_row, to_col):
        from_row, from_col = self.get_position()

        # Verifica que el alfil se mueva en linea diagonal
        if from_row == to_row or from_col == to_col:
                raise InvalidMoveBishop("El alfil no se puede mover en forma Horizontal o Vertical")
        
        if self.diagonal_move(to_row, to_col):
            return True