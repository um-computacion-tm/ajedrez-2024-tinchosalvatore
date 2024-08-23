from main.board import Board
from main.exceptions import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def turn(self):
        return self.__turn__
    
    def move(self, from_row, from_col, to_row, to_col):
        piece_color = self.__board__.get_color(from_row, from_col)
        
        if piece_color is None:
            raise InvalidMoveNoPiece("No hay pieza en esa posicion")
        if self.__turn__ != piece_color:
            raise InvalidMovePieceFromOtherColor("La pieza es del enemigo")
        
        result = self.__board__.move_piece(from_row, from_col, to_row, to_col)
        if result:
            self.change_turn()
            return True
        self.change_turn()
        return False
    
    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
    
    def show_board(self):
        return self.__board__.show_board()
    
    def is_playing(self):
        return True