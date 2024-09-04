from main.board import Board
from main.exceptions import *
from main.pawn import Pawn

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True
        self.__pawn__ = Pawn

    def turn(self):
        return self.__turn__

    def piece(self, from_row, from_col): # Metodo que obtiene una pieza
        piece = self.__board__.get_piece(from_row, from_col)
        return piece

    # Captura la pieza en la posicion indicada
    def capture_piece(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)
        if piece is None:
            return None  

        if self.ocuppied_path(from_row, from_col, to_row, to_col):
            raise InvalidMovePathOcuppied("Hay una pieza que bloquea el camino")

        target_piece = self.__board__.get_piece(to_row, to_col)
        if target_piece and target_piece.get_color() != piece.get_color():
            self.__board__.remove_piece(to_row, to_col)  # Remove the captured piece
            self.__board__.set_piece(None, from_row, from_col)
            self.__board__.set_piece(piece, to_row, to_col)
            return True
        return False
    
    def pawn_capture(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)
        if isinstance(piece, Pawn):
            there_is_a_piece = self.__board__.get_piece(to_row, to_col)
            if there_is_a_piece is not None and there_is_a_piece.get_color() != piece.get_color():
                if piece.diagonal_pawn_movement(from_row, from_col, to_row, to_col):
                    self.__board__.remove_piece(to_row, to_col)
                    self.__board__.set_piece(None, from_row, from_col)
                    self.__board__.set_piece(piece, to_row, to_col)
                    return True
        return False

    def ocuppied_path(self, from_row, from_col, to_row, to_col):
        return self.__board__.occupied_path_vertical_horizontal(from_row, from_col, to_row, to_col) or \
            self.__board__.occupied_path_diagonal(from_row, from_col, to_row, to_col)
    
    def pieces_movements(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)
        if isinstance(piece, Pawn):
            if self.pawn_capture(from_row, from_col, to_row, to_col):
                self.change_turn()
                return True  # Se habilita el movimiento diagonal del peon para capturar

            elif not piece.valid_moves_pawn(from_row, from_col, to_row, to_col):
                raise InvalidMoveNotAllowed("No es un movimiento válido para el peón")
        else:
            if not piece.valid_moves(from_row, from_col, to_row, to_col):
                raise InvalidMoveNotAllowed("No es un movimiento válido para esa pieza")

    # Mueve las piezas y las captura
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.piece(from_row, from_col)

        if self.__board__.get_piece(from_row, from_col) is None:
            raise InvalidMoveNoPiece("No hay pieza en esa posicion")
        
        if self.__turn__ != self.__board__.get_color(from_row, from_col):
            raise InvalidMovePieceFromOtherColor("La pieza es del enemigo")

        if self.__turn__ == self.__board__.get_color(to_row, to_col):
            raise InvalidMoveSameColor("La posicion tiene una pieza del mismo color")
        
        if self.pieces_movements(from_row, from_col, to_row, to_col):
            return True

        if self.ocuppied_path(from_row, from_col, to_row, to_col):
            raise InvalidMovePathOcuppied("Hay una pieza que bloquea el camino")

        if self.capture_piece(from_row, from_col, to_row, to_col):
            self.change_turn()
            return True  # Pieza en el destino es del enemigo y se captura
        
        if self.pawn_capture(from_row, from_col, to_row, to_col):
            self.change_turn()
            return True  # Se habilita el movimiento diagonal del peon para capturar

        
        self.__board__.set_piece(None, from_row, from_col)
        self.__board__.set_piece(piece, to_row, to_col)
        self.change_turn()
        return True
        

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def show_board(self):
        return self.__board__.show_board()

    def is_playing(self):
        return self.__playing__
    
    def end_game(self):
        self.__playing__ = False  # Cambiar el estado del juego a "no en curso"
        print("El usuario terminó el juego.")