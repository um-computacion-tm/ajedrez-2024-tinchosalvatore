from pieces import Rook

class Board:
    def __init__(self):
        self.__position__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__position__.append(col)
        self.__position__[0][0] =  Rook("BLACK")
        self.__position__[0][7] =  Rook("BLACK")
        
        self.__position__[7][0] =  Rook("WHITE")    
        self.__position__[7][7] =  Rook("WHITE")

    def get_piece(self, row, col):
        return self.__position__[row][col]
    