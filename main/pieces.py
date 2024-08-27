class Piece:
    def __init__(self, color, row=None, col=None):
        self.__color__ = color
        self.__row__ = row
        self.__col__ = col

    def __str__(self):
        ...

    def set_position(self, row, col):
        self.__row__ = row
        self.__col__ = col

    def get_position(self):
        return self.__row__, self.__col__

    def get_color(self):
        return self.__color__