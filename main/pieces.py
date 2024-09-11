class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        ...

    def get_color(self):
        return self.__color__