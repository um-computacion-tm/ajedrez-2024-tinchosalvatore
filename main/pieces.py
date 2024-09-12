class Piece:

    #Piece class is the base class for all the pieces
    #They get their color and str method from here :)

    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        ...

    def get_color(self):
        return self.__color__