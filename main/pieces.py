class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        ...

    def get_color(self):
        return self.__color__
    
    def valid_moves(self, from_row, from_col, to_row, to_col):
        ...