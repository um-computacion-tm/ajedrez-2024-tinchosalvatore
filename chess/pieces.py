class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__position__ = None

    def set_position(self, row, col):
        self.__position__ = (row, col)

    def move (self, row, col):
        self.set_position(row, col)

    def __str__(self): # Retorna la primera letra del nombre de la clase
        representation = self.__class__.__name__[0]
        return representation.lower() if self.__color__ == "WHITE" else representation.upper() 

    def is_valid_move(self, move):
        ...
    
    def get_color(self):
        return self.__color__