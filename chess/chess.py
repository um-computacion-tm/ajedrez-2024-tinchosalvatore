from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def turn(self):
        return self.__turn__
    
    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col) #obtiene posicion inicial
        if piece and piece.get_color() == self.__turn__:
            result = self.__board__.move_piece((from_row, from_col, to_row, to_col))
            if result is not None:
                self.change_turn()
                return True
            else:
                return False
        else:
            return False

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
    
    def show_board(self):
        return self.__board__.show_board()
    
    def is_playing(self):
        return True