from main.pieces import Piece
from main.exceptions import *

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"
        
    def initial_position(self, row):
        return (self.__color__ == "WHITE" and row == 6) or (self.__color__ == "BLACK" and row == 1)

    def valid_moves(self, from_row, from_col, to_row, to_col):
        direction = -1 if self.__color__ == "WHITE" else 1
        row_diff = to_row - from_row
        col_diff = abs(to_col - from_col)

        # Movimiento hacia adelante
        if from_col == to_col:
            if row_diff * direction <= 0:
                raise InvalidMovePawn("El peón no puede moverse hacia atrás")
            if self.initial_position(from_row):
                if row_diff == direction or row_diff == 2 * direction:
                    return True
                else:
                    raise InvalidMovePawn("El peón solo puede avanzar 1 o 2 casillas en su primer movimiento")
            else:
                if row_diff == direction:
                    return True
                else:
                    raise InvalidMovePawn("El peón solo puede avanzar 1 casilla")
        # Movimiento diagonal (potencial captura)
        elif col_diff == 1 and row_diff == direction:
            return True
        else:
            raise InvalidMovePawn("Movimiento de peón inválido")

    def is_valid_capture(self, from_row, from_col, to_row, to_col):
        direction = -1 if self.__color__ == "WHITE" else 1
        row_diff = to_row - from_row
        col_diff = abs(to_col - from_col)
        return col_diff == 1 and row_diff == direction