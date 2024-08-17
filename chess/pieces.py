class Piece:
    def __init__(self, color):
        self.__color__ = color

    def is_valid_move(self, move):
        ...
    
    def get_color(self):
        return self.__color__

    def get_name(self):
        return self.__name__