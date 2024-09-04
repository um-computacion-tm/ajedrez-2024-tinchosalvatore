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

    def pawn_jump(self, from_row, from_col, to_row, to_col):
        direction = self.pawn_direction(from_row, from_col, to_row, to_col)
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        
        if not (row_diff == 0 and col_diff == 2):
            raise InvalidMovePawn("El peon inicialmente solo puede moverse 1 o 2 casillas")
    
        return 1 if to_col > from_col else -1

    def vertical_pawn_move(self, from_row, from_col, to_row, to_col): 
        direction = self.pawn_direction(from_row, from_col, to_row, to_col)

        # El peón solo puede moverse en su columna actual.
        if from_col != to_col:
            raise InvalidMovePawn("El peón no puede moverse horizontalmente sin capturar")

        # El peón puede moverse cualquier número de casillas hacia adelante.
        if (to_row - from_row) * direction <= 0:
            raise InvalidMovePawn("El peón solo puede moverse hacia adelante")

        return True  # El movimiento es válido si no se lanza ninguna excepción.

    def pawn_capture(self, from_row, from_col, to_row, to_col):
        direction = self.pawn_direction()
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            return True
        
    def valid_moves(self, from_row, from_col, to_row, to_col):
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