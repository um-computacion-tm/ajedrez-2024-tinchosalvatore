from main.pieces import Piece
from main.movements import ReglasDeMovimientos
from main.exceptions import *

class Pawn(Piece):

    #Pawm class is a particular case, and a very irritating one
    #Its movement is made here and not in the movements class because of how particular it is

    def __init__(self, color):
        super().__init__(color)
        self.__movimientos__ = ReglasDeMovimientos()
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"
    
    def pawn_initial_position(self, from_row):
        #This method define the initial row position of the pawn, depending on the color
        #Later it would be used if the pawn is able to do a double jump on its first move
        if self.get_color() == "WHITE":
            return from_row == 6
        else:
            return from_row == 1
    
    def pawn_direction(self): 
        #This method returns the direction of the pawn, depending on the color
        #This is done cause the pawn is not able to move backwards
        direction = -1 if self.get_color() == "WHITE" else 1
        return direction

    def diagonal_pawn_movement(self, from_row, from_col, to_row, to_col):
        #Diagonal pawn movement for captures
        direction = self.pawn_direction()
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            return True
    
    def valid_moves_pawn(self, from_row, from_col, to_row, to_col):
        direction = self.pawn_direction()
        
        #Inicial vertical move for pawn of 1 or 2 squares
        if from_col == to_col:
            if to_row == from_row + direction:
                return True  #One square movement
            elif to_row == from_row + 2 * direction and self.pawn_initial_position(from_row):
                return True  #Two squares movement if it is on the initial position
            else: #Exception in case of invalid movement for the pawn
                raise InvalidMovePawn("Movimiento inválido para el peón")