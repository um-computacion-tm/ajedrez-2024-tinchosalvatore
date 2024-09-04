from main.pieces import Piece
from main.movements import ReglasDeMovimientos
from main.exceptions import *

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__movimientos__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"
    
    def pawn_initial_position(self, from_row):
        if self.get_color() == "WHITE":
            return from_row == 6
        else:
            return from_row == 1
    
    def pawn_direction(self):
        direction = -1 if self.get_color() == "WHITE" else 1
        return direction

    def diagonal_pawn_movement(self, from_row, from_col, to_row, to_col):
        direction = self.pawn_direction()
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            return True
        return False
    
    def valid_moves_pawn(self, from_row, from_col, to_row, to_col):
        direction = self.pawn_direction()
        
        # Movimiento vertical inicial de 1 o 2 casillas
        if from_col == to_col:
            if to_row == from_row + direction:
                return True  # Movimiento de una casilla
            elif to_row == from_row + 2 * direction and self.pawn_initial_position(from_row):
                return True  # Movimiento de dos casillas en la posición inicial
            else:
                raise InvalidMovePawn("Movimiento inválido para el peón")
            
        # Movimiento no válido
        else:
            raise InvalidMovePawn("Movimiento inválido para el peón")