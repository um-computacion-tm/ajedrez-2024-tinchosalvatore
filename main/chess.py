from main.board import Board
from main.exceptions import *

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def turn(self):
        return self.__turn__
    
    # Captura la pieza en la posicion indicada
    def capture_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            return None  # No piece at the start position

        target_piece = self.__board__.get_piece(to_row, to_col)
        if target_piece and target_piece.get_color() != piece.get_color():
            self.__board__.remove_piece(to_row, to_col)  # Remove the captured piece
            self.__board__.__positions__[from_row][from_col] = None
            self.__board__.__positions__[to_row][to_col] = piece
            piece.__board__.set_position(to_row, to_col)
            return True
        
    # Mueve la pieza y detecta si no hay pieza en esa posicion y si el destino esta ocupado
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
         
        target_piece = self.__board__.get_piece(to_row, to_col)
        if target_piece and target_piece.get_color() == piece.get_color():
            raise InvalidMoveSameColor("La posicion tiene una pieza del mismo color")

        #if self.is_valid_move(to_row, to_col, self):
        if self.capture_piece(from_row, from_col, to_row, to_col):
            return True  # Pieza en el destino es del enemigo y se captura
        
        # Mueve la pieza
        #if self.is_valid_move(to_row, to_col, self):
            self.__positions__[from_row][from_col] = None
            self.__positions__[to_row][to_col] = piece
            piece.set_position(to_row, to_col)
            return True
        #else:
        #    raise InvalidMove("Movimiento invalido")


    def move(self, from_row, from_col, to_row, to_col):
        move_piece_color = self.__board__.get_color(from_row, from_col)
        final_piece_color = self.__board__.get_color(to_row, to_col)
        
        if move_piece_color is None:
            raise InvalidMoveNoPiece("No hay pieza en esa posicion")
        
        if self.__turn__ != move_piece_color:
            raise InvalidMovePieceFromOtherColor("La pieza es del enemigo")
        
        if move_piece_color == final_piece_color:
            raise InvalidMoveSameColor("La posicion tiene una pieza del mismo color")
        
        result = self.move_piece(from_row, from_col, to_row, to_col)
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