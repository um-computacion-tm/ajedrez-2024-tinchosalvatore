from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def turn(self):
        return self.__turn__
    
    def move(self, from_row, from_col, to_row, to_col): 
        piece = self.__board__.get_piece(from_row, from_col)
        if piece and piece.get_color() ==  self.__turn__:
            if piece.is_valid_move((to_row, to_col)): 
                self.__board__.move_piece(from_row, from_col, to_row, to_col)
                self.change_turn()
            else:
                return None
        else:
            return False

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
    
    def show_board(self):
        return self.__board__.show_board()