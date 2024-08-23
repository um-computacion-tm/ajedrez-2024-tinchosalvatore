class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__position__ = None

    def __str__(self):
        ...

    def set_position(self, row, col):
        self.__position__ = (row, col)

    def move (self, row, col):
        self.set_position(row, col)

    def diagonal_move(self, row, col):
        ...
    def horizontal_move(self, row, col):
        ...

    def is_valid_move(self, move):
        ...
    
    def get_color(self):
        return self.__color__