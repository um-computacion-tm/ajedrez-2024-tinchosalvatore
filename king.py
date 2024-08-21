from pieces import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♔"
        else:
            return "♚"